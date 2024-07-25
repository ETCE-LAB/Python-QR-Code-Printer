# BrotherQrPrinter

## Description
BrotherQrPrinter is a Python application designed for managing tool inventories. It interfaces with Brother QR printers to generate and print QR codes, each containing a UUID specific to the tool.
This system streamlines the tracking and management of tools in an inventory environment.

## Installation

### Prerequisites
- Python 3.x
- pip

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/BrotherQrPrinter.githttps://github.com/MattesKnigge/BrotherQrPrinter.git
   ```
2. Navigate to the project directory:
   ```
   cd BrotherQrPrinter
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
## Troubleshooting
**Before running** the application, execute the `patch_conversion.py` script to ensure compatibility with the latest version of Pillow. This script will update a line in the `conversion.py` file within the `brother_ql` package to use modern image resizing methods.

To run the script, use:
```
python patch_conversion.py
```
If your virtual enviroment has a different name than `venv` update it inside the `patch_conversion.py` script.
This will automatically apply the necessary change and create a backup of the original file as `conversion.py.bak`.

## Usage
To start the application, run:
```
python app.py
```
The server will start, and you can interact with the API to print QR codes.

## Configuration
Modify the `config` directory files to adjust the application settings according to your printer model and network configuration.

## Testing
Run the following command to execute the tests:
```
python -m unittest discover tests
```

## Authors
- **Mattes Knigge** - *Initial work for ETCE-LAB* - [MattesKnigge](https://github.com/MattesKnigge)
