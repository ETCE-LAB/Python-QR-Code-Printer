import logging
import tempfile
from PIL import Image, ImageDraw
import qrcode
from brother_ql.raster import BrotherQLRaster
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
import traceback
from config.config import (
    PRINTER_NAME, LABEL_TYPE, LABEL_WIDTH, LABEL_HEIGHT, FONT_PATH, FONT_SIZE
)
from utils.utils import load_font, resize_image
from errors.errors import CustomError

logger = logging.getLogger(__name__)


def create_qr_code(data, id_text, name_text):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,  # Adjusted for demonstration; you might need to tweak this
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

        font = load_font(FONT_PATH, FONT_SIZE)
        draw = ImageDraw.Draw(qr_img)

        # Calculate text size and position for the ID text
        id_bbox = draw.textbbox((0, 0), id_text, font=font)
        id_width = id_bbox[2] - id_bbox[0]
        id_height = id_bbox[3] - id_bbox[1]

        # Calculate text size and position for the name text
        name_bbox = draw.textbbox((0, 0), name_text, font=font)
        name_width = name_bbox[2] - name_bbox[0]
        name_height = name_bbox[3] - name_bbox[1]

        # Calculate the combined image dimensions
        max_text_width = max(id_width, name_width)
        combined_img_width = max(qr_img.width, max_text_width)
        combined_img_height = qr_img.height + id_height + name_height + 30  # Adjust spacing

        combined_img = Image.new('RGB', (combined_img_width, combined_img_height), 'white')
        qr_img_x_center = (combined_img_width - qr_img.width) // 2
        combined_img.paste(qr_img, (qr_img_x_center, 0))

        draw = ImageDraw.Draw(combined_img)

        # Draw the ID text centered above the name
        id_x_center = (combined_img_width - id_width) // 2
        draw.text((id_x_center, qr_img.height + 10), id_text, fill='black', font=font)

        # Draw the name text centered below the ID
        name_x_center = (combined_img_width - name_width) // 2
        draw.text((name_x_center, qr_img.height + id_height + 20), name_text, fill='black', font=font)

        return combined_img
    except Exception as e:
        logger.error(f"Error creating QR code: {e}")
        logger.error(traceback.format_exc())
        raise CustomError(f"Error creating QR code: {e}", status_code=400)


def print_qr_code(image, rotate='0'):
    qlr = BrotherQLRaster('QL-800')

    try:
        resized_image = resize_image(image, (LABEL_WIDTH, LABEL_HEIGHT))
        expanded_height = LABEL_HEIGHT + 5
        expanded_image = Image.new('RGB', (LABEL_WIDTH, expanded_height), 'white')
        expanded_image.paste(resized_image, (0, 0))
    except RuntimeError as e:
        logger.error(f"Error preparing image for printing: {e}")
        logger.error(traceback.format_exc())
        raise CustomError(f"Error preparing image for printing: {e}", status_code=424)

    try:
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            expanded_image.save(tmp.name)
            convert(qlr, [tmp.name], LABEL_TYPE, rotate=rotate)
            send(qlr.data, PRINTER_NAME, backend_identifier='pyusb', blocking=True)
    except ValueError as e:
        if str(e) == 'Device not found':
            logger.error(f"Printer not found: {e}")
            logger.error(traceback.format_exc())
            raise CustomError("Printer not connected or not found", status_code=503)
        else:
            logger.error(f"Unexpected error during printing: {e}")
            logger.error(traceback.format_exc())
            raise CustomError(f"Unexpected error during printing: {e}", status_code=500)
    except IOError as e:
        logger.error(f"IOError during image conversion or sending: {e}")
        logger.error(traceback.format_exc())
        raise CustomError(f"IOError during image conversion or sending: {e}", status_code=500)
    except Exception as e:
        logger.error(f"Unexpected error printing QR code: {e}")
        logger.error(traceback.format_exc())
        raise CustomError(f"Unexpected error printing QR code: {e}", status_code=500)

    return {"status": "Print successfully completed"}, 200
