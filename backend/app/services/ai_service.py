from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


class MaterialCreate(BaseModel):
    title: str
    content: str
    source_name: Optional[str] = None
    user_id: int


class StudyAskRequest(BaseModel):
    question: str
    user_id: int


class StudySummaryRequest(BaseModel):
    user_id: int


class FlashcardRequest(BaseModel):
    user_id: int
    material_id: Optional[int] = None


class QuizRequest(BaseModel):
    user_id: int
    material_id: Optional[int] = None
