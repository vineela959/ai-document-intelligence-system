from docx import Document


def read_docx(file):

    text = ""

    doc = Document(file)

    for paragraph in doc.paragraphs:
        text += paragraph.text

    return text