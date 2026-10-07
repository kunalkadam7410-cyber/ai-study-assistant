# AI Study Assistant

An AI-powered study assistant that helps students upload learning material, ask questions, generate flashcards, and take quizzes.

## Features

- Upload PDFs and text documents
- Ask questions grounded in your uploaded materials
- Generate summaries and study notes
- Create flashcards automatically
- Generate multiple-choice quizzes
- Track study progress with a simple dashboard
- Modern UI with Next.js and Tailwind CSS

## Tech Stack

- Frontend: Next.js + TypeScript + Tailwind CSS
- Backend: FastAPI + Python
- Database: SQLite (easy local dev)
- AI: OpenAI API optional; mock fallback included for local testing
- Vector search: in-memory fallback, ready for Pinecone/pgvector extension

## Project Structure

- `backend/` – FastAPI API and business logic
- `frontend/` – Next.js app
- `README.md` – project setup and usage
- `.env.example` – example environment variables

## Quick Start

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
uvicorn app.main:app --reload --port 8000
```

### 2) Frontend

```bash
cd frontend
npm install
cp ../.env.example .env.local
npm run dev
```

### 3) Open the app

- Frontend: http://localhost:3000
- API docs: http://localhost:8000/docs

## Environment Variables

Copy `.env.example` to `.env` and configure:

```env
OPENAI_API_KEY=your_key_here
BACKEND_URL=http://localhost:8000
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Example Workflow

1. Create an account or log in
2. Upload one or more notes/documents
3. Ask: “Explain the difference between mitosis and meiosis”
4. Generate flashcards or a quiz from the uploaded material
5. Track your progress in the dashboard

## Notes

This project is designed as a production-ready starter for an AI study app, with room to extend it with vector database indexing, authentication, scheduling, and advanced analytics.
