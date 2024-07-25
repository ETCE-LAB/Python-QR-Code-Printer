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
3. Create a virtual enviroment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment using the appropriate command for your operating system:
   
   **Linux and macOS:**
   ```
   source venv/bin/activate
   ```
   **Windows:**
   ```
   .\venv\Scripts\activate
   ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
## Troubleshooting
**Before running** the application, navigate to the following file: `venv/Lib/site-packages/brother_ql/conversion.py`. Please note that the exact path may vary depending on your operating system.

In this file, locate line 115 and modify it as follows:
```python
im = im.resize((dots_printable[0], hsize), Image.Resampling.LANCZOS)
```
This change is necessary to fix an error with the brother_ql library, which is caused by it using an older version of the Pillow library than required.

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
