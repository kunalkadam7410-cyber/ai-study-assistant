from sqlalchemy.orm import Session

from app.models import User, Material, StudySession, Flashcard, QuizQuestion


def create_user(db: Session, name: str, email: str, password_hash: str) -> User:
    user = User(name=name, email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_material(db: Session, user_id: int, title: str, content: str, source_name: str | None = None) -> Material:
    material = Material(user_id=user_id, title=title, content=content, source_name=source_name)
    db.add(material)
    db.commit()
    db.refresh(material)
    return material


def get_user_materials(db: Session, user_id: int):
    return db.query(Material).filter(Material.user_id == user_id).all()


def save_flashcards(db: Session, user_id: int, material_id: int | None, flashcards: list[dict]):
    saved = []
    for item in flashcards:
        card = Flashcard(front=item["front"], back=item["back"], user_id=user_id, material_id=material_id)
        db.add(card)
        db.commit()
        db.refresh(card)
        saved.append(card)
    return saved


def save_quiz_questions(db: Session, user_id: int, material_id: int | None, questions: list[dict]):
    saved = []
    for item in questions:
        question = QuizQuestion(
            question=item["question"],
            options=str(item["options"]),
            correct_answer=item["correct_answer"],
            explanation=item.get("explanation"),
            user_id=user_id,
            material_id=material_id,
        )
        db.add(question)
        db.commit()
        db.refresh(question)
        saved.append(question)
    return saved


def get_dashboard_stats(db: Session, user_id: int):
    materials_count = db.query(Material).filter(Material.user_id == user_id).count()
    flashcards_count = db.query(Flashcard).filter(Flashcard.user_id == user_id).count()
    quiz_count = db.query(QuizQuestion).filter(QuizQuestion.user_id == user_id).count()
    return {
        "materials_count": materials_count,
        "flashcards_count": flashcards_count,
        "quiz_count": quiz_count,
    }
