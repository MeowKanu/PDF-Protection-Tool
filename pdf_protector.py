import sys
import PyPDF2


def create_password_protected_pdf(input_pdf, output_pdf, password):
    try:
        # Open the input PDF
        with open(input_pdf, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # Create writer
            pdf_writer = PyPDF2.PdfWriter()

            # Copy pages
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # Apply encryption
            pdf_writer.encrypt(password)

            # Write output PDF
            with open(output_pdf, "wb") as output:
                pdf_writer.write(output)

        print(f"Success! Encrypted PDF saved as: {output_pdf}")

    except FileNotFoundError:
        print("❌ Error: Input PDF file not found.")
    except PyPDF2.errors.PdfReadError:
        print("❌ Error: Unable to read the PDF (corrupted or invalid file).")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def main():
    # Check arguments
    if len(sys.argv) != 4:
        print("Usage: python pdf_protector.py <input.pdf> <output.pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    create_password_protected_pdf(input_pdf, output_pdf, password)


if __name__ == "__main__":
    main()
