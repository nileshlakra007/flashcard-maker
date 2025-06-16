from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from backend.utils.pdf_parser import extract_text_from_pdf
from backend.utils.chunker import split_text_into_chunks
from backend.utils.openai_client import generate_flashcards
import tempfile
import os

app = FastAPI()


@app.post('/generate-flashcards')
async def generate_flashcards_endpoint(file: UploadFile = File(...)):
    if file.content_type not in ['application/pdf', 'text/plain']:
        raise HTTPException(status_code=400, detail='Unsupported file type')

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    try:
        if file.content_type == 'application/pdf':
            text = extract_text_from_pdf(tmp_path)
        else:
            text = contents.decode('utf-8')
    finally:
        os.unlink(tmp_path)

    chunks = split_text_into_chunks(text)
    flashcards = []
    for chunk in chunks:
        flashcards.extend(generate_flashcards(chunk))

    return JSONResponse([{"question": q, "answer": a} for q, a in flashcards])
