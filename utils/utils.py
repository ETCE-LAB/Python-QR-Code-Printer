import logging
from PIL import ImageFont, Image, UnidentifiedImageError
import traceback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_font(font_path=None, font_size=10):
    try:
        if font_path:
            return ImageFont.truetype(font_path, font_size)
        else:
            return ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        logger.error("Font not found, using default font")
        return ImageFont.load_default()


def resize_image(image, size):
    try:
        if hasattr(Image, 'Resampling'):
            resampling = Image.Resampling.LANCZOS
        else:
            raise AttributeError("Pillow version does not support Image.Resampling.LANCZOS")
        return image.resize(size, resampling)
    except UnidentifiedImageError as e:
        logger.error(f"Error resizing image: {e}")
        logger.error(traceback.format_exc())
        raise e
    except Exception as e:
        logger.error(f"Unexpected error resizing image: {e}")
        logger.error(traceback.format_exc())
        raise e
