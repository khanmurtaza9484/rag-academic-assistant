# Import the PDF reader library
from pypdf import PdfReader


def extract_text(pdf_path):
    """
    Reads a PDF file and extracts all text.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Complete extracted text from the PDF.
    """

    # Open the PDF file
    reader = PdfReader(pdf_path)

    text = ""

    # Read text from each page
    for page in reader.pages:
        page_text = page.extract_text()

        # Skip pages with no readable text
        if page_text:
            text += page_text + "\n"

    # Return the extracted text
    return text
