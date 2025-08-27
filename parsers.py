import os

import pdfplumber
import docx2python


def extract_text_from_pdf(filepath: str) -> str:
    """Extract all text from a PDF file."""
    text = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)


def extract_text_from_docx(filepath: str) -> str:
    """Extract all text from a DOCX file."""
    result = docx2python.docx2python(filepath)
    paragraphs = []
    for section in result.body:
        for paragraph in section:
            if paragraph:
                paragraphs.append("".join(paragraph))
    return "\n".join(paragraphs)


def extract_text(filepath: str) -> str:
    """Determine file type by extension and extract text accordingly."""
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    if ext in (".docx", ".doc"):
        return extract_text_from_docx(filepath)
    raise ValueError(f"Unsupported file extension: {ext}")