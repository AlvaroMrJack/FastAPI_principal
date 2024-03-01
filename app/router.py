from fastapi import Body, Depends, APIRouter
from schemas.responses import GeneralResponse
from models.incidencia import Incidencia
from schemas.alarma import AlarmaBase
from schemas.incidencia import IncidenciaBase, IncidenciaCreate
from api.alarma.alarma import get_alarmas, get_alarma
from api.incidencia.incidencia import create_incidencia
from database.settings import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def bienvenido():
    return {"Hola SBW"}

@router.get("/alarmas/", response_model=list[AlarmaBase])
async def listado_alarmas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alarms = await get_alarmas(skip=skip, limit=limit, db=db)
    return alarms

@router.get("/alarma/{id}", response_model=AlarmaBase)
async def leer_alarma(id = 0, db: Session = Depends(get_db)):
    alarms = await get_alarma(id=id, db=db)
    return alarms

@router.post("/crear_incidencia/", response_model=GeneralResponse)
async def crear_incidencia(incidencia: IncidenciaCreate = Body(..., embed=True), db: Session = Depends(get_db)):
    incidencia = await create_incidencia(incidencia=incidencia, db=db)
    response = GeneralResponse(
        estado="success",
        icono="check",
        validacion="success",
        mensaje="Incidencia creada correctamente",
        dotacion_id=incidencia.dotacion_id
    )
    return response