from sqlalchemy.orm import Session
from models.incidencia import Incidencia
from schemas.incidencia import IncidenciaCreate

async def create_incidencia(db: Session, incidencia: IncidenciaCreate):
    db_incidencia = Incidencia(**incidencia.model_dump())
    db.add(db_incidencia)
    db.commit()
    db.refresh(db_incidencia)
    return db_incidencia