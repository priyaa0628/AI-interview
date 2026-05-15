import PyPDF2


def extract_text_from_pdf(uploaded_file):

    # Read uploaded PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    # Store all text
    text = ""

    # Read each page
    for page in pdf_reader.pages:

        # Extract page text
        text += page.extract_text()

    return text