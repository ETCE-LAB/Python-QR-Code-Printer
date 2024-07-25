import fileinput
import sys


def update_file():
    file_path = 'venv/lib/python3.12/site-packages/brother_ql/conversion.py'  # Replace with the path to the file on your system
    target_line = 115                                                         # Replace with the line number you want to update
    old_text = 'Image.ANTIALIAS'
    new_text = 'Image.Resampling.LANCZOS'

    with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for i, line in enumerate(file):
            if i + 1 == target_line and old_text in line:
                line = line.replace(old_text, new_text)
            else:
                print('Target line not found in the file. Please check the file path and target line number.')
                print('Found line:', line, end='')
            sys.stdout.write(line)

    print(f"File {file_path} updated successfully")


if __name__ == '__main__':
    update_file()
