from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import get_user_materials, save_flashcards, save_quiz_questions
from app.db import get_db
from app.schemas import StudyAskRequest, FlashcardRequest, QuizRequest
from app.services.ai_service import AIStudyService

router = APIRouter()


@router.post("/ask")
def ask_question(payload: StudyAskRequest, db: Session = Depends(get_db)):
    materials = get_user_materials(db, payload.user_id)
    context = "\n\n".join(item.content for item in materials)
    service = AIStudyService()
    answer = service.answer_question(payload.question, context)
    return {"answer": answer}


@router.post("/summary")
def generate_summary(payload: StudyAskRequest, db: Session = Depends(get_db)):
    materials = get_user_materials(db, payload.user_id)
    text = "\n\n".join(item.content for item in materials)
    if not text:
        raise HTTPException(status_code=400, detail="No materials found for this user")
    service = AIStudyService()
    return {"summary": service.summarize(text)}


@router.post("/flashcards")
def generate_flashcards(payload: FlashcardRequest, db: Session = Depends(get_db)):
    materials = get_user_materials(db, payload.user_id)
    if not materials:
        raise HTTPException(status_code=400, detail="No materials found for this user")
    material = next((m for m in materials if m.id == payload.material_id), materials[0])
    service = AIStudyService()
    cards = service.generate_flashcards(material.content)
    saved = save_flashcards(db, payload.user_id, material.id, cards)
    return {"flashcards": [{"front": item.front, "back": item.back} for item in saved]}


@router.post("/quiz")
def generate_quiz(payload: QuizRequest, db: Session = Depends(get_db)):
    materials = get_user_materials(db, payload.user_id)
    if not materials:
        raise HTTPException(status_code=400, detail="No materials found for this user")
    material = next((m for m in materials if m.id == payload.material_id), materials[0])
    service = AIStudyService()
    questions = service.generate_quiz(material.content)
    saved = save_quiz_questions(db, payload.user_id, material.id, questions)
    return {"quiz": [{"question": item.question, "options": item.options, "correct_answer": item.correct_answer, "explanation": item.explanation} for item in saved]}
