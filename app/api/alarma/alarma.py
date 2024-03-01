from sqlalchemy.orm import Session
from models.alarma import Alarma

async def get_alarmas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Alarma).offset(skip).limit(limit).all()

async def get_alarma(db: Session, id: int):
    return db.query(Alarma).filter(Alarma.id == id).first()