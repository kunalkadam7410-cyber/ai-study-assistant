from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import get_dashboard_stats
from app.db import get_db

router = APIRouter()


@router.get("/{user_id}")
def dashboard_stats(user_id: int, db: Session = Depends(get_db)):
    return get_dashboard_stats(db, user_id)
