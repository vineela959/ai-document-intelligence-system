from pypdf import PdfReader


def read_pdf(file):

    text = ""

    reader = PdfReader(file)

    for page in reader.pages:
        text += page.extract_text()

    return text