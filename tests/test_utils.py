import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import base64

from backend.utils.pdf_parser import extract_text_from_pdf
from backend.utils.chunker import split_text_into_chunks


def test_extract_text_from_pdf(tmp_path):
    b64_path = os.path.join(os.path.dirname(__file__), 'resources', 'sample_pdf.b64')
    pdf_bytes = base64.b64decode(open(b64_path).read())
    pdf_file = tmp_path / 'sample.pdf'
    pdf_file.write_bytes(pdf_bytes)
    text = extract_text_from_pdf(str(pdf_file))
    assert 'Hello World' in text


def test_split_text_into_chunks():
    text = ' '.join(['word.'] * 50)
    chunks = split_text_into_chunks(text, max_tokens=20)
    assert len(chunks) >= 2
