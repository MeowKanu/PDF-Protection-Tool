PDF Protection Tool

This project is a simple Python-based tool used to add password protection to any PDF file using the PyPDF2 library. It is designed for beginners and students learning file handling, exception handling, and PDF manipulation in Python.

Features

Add password encryption to any existing PDF

Retains original pages and formatting

Uses PyPDF2 (lightweight and easy to use)

Includes error handling for missing or corrupted files

Runs directly from the command line

Project Structure
pdf-protection-tool/
│── pdf_protector.py       # Main script
│── README.md              # Documentation
└── sample.pdf             # Optional test file

Installation

Make sure Python is installed. Then install PyPDF2:

pip install PyPDF2

Usage

Run the script from the command line:

python pdf_protector.py <input.pdf> <output.pdf> <password>


Example:

python pdf_protector.py sample.pdf protected.pdf mypassword123


The file "protected.pdf" will now require the password "mypassword123" to open.

How It Works

The script reads the original PDF using PyPDF2.PdfReader

Copies all pages into a PdfWriter object

Encrypts the output PDF using the user-provided password

Saves the password-protected PDF to the specified output path

Requirements

Python 3.7 or higher

PyPDF2 library

Error Handling

The script handles:

File not found errors

Invalid or corrupted PDFs

Unexpected runtime errors

Contributing

Feel free to fork this repository and submit pull requests or issues.

License

This project is licensed under the MIT License.
