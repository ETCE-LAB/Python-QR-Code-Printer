
# Python-QR-Code-Printer

## Description

Python-QR-Code-Printer is a Python application that is part of a larger project for managing tool inventories. The code within this repository focuses specifically on connecting to the Brother-QL-800 printer and printing QR codes.
This component interfaces with Brother QR printers to generate and print QR codes, each containing a UUID specific to the tool. This system streamlines the tracking and management of tools in an inventory environment.

## Installation

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/ETCE-LAB/Python-QR-Code-Printer.git
   ```
2. Navigate to the project directory:
   ```
   cd Python-QR-Code-Printer
   ```
3. Create a virtual environment:
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

In this file, locate line 115 which will look like this:
```python
im = im.resize((dots_printable[0], hsize), Image.ANTIALIAS)
```
**Now you have to change it to:**
```python
im = im.resize((dots_printable[0], hsize), Image.Resampling.LANCZOS)
```
This change is necessary to fix an error with the `brother_ql` library, which is caused by it using an older version of the Pillow library than required.

## Usage

To start the application, run:
```
python app.py
```
The server will start, and you can interact with the API to print QR codes.


## Authors

- **Mattes Knigge** - *Initial work for ETCE-LAB* - [MattesKnigge](https://github.com/MattesKnigge)
