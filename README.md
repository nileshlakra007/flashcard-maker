# AI Flashcard Generator

This project contains a minimal prototype for generating flashcards from PDF or text files using OpenAI GPT models. It consists of a FastAPI backend and a React frontend built with Vite.

## Backend

- **Endpoint:** `POST /generate-flashcards`
  - Accepts a PDF or text file and returns generated flashcards as JSON.
- Utilities for extracting text from PDFs, splitting text into manageable chunks and calling the OpenAI API.
- Run with `uvicorn backend.main:app --reload` after installing dependencies with `pip install -r backend/requirements.txt`.

## Frontend

- Simple UI allowing file upload and displaying generated flashcards.
- Start with `npm install` and `npm run dev` inside the `frontend` folder.

## Tests

Unit tests for backend utilities can be executed with `pytest` from the project root.
