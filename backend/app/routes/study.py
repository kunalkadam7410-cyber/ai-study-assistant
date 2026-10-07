from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session

from app.crud import create_material, get_user_materials
from app.db import get_db

router = APIRouter()


@router.get("/{user_id}")
def list_documents(user_id: int, db: Session = Depends(get_db)):
    materials = get_user_materials(db, user_id)
    return [{"id": item.id, "title": item.title, "source_name": item.source_name, "content": item.content[:200]} for item in materials]


@router.post("/upload")
async def upload_document(
    user_id: int = Form(...),
    title: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    contents = await file.read()
    text = contents.decode("utf-8", errors="ignore")
    if not text.strip():
        raise HTTPException(status_code=400, detail="Uploaded file has no readable text")

    material = create_material(db, user_id=user_id, title=title or file.filename, content=text, source_name=file.filename)
    return {"id": material.id, "title": material.title, "source_name": material.source_name}
