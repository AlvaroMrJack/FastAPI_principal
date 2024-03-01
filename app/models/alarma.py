from datetime import datetime
import sqlalchemy
from database.settings import Base
from pydantic import BaseModel
from typing import Optional

class Alarma(Base):
    __tablename__ = "alarma"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    dotacion_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    fecha_registro = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    fecha_persecucion = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    dotacion_id_persecucion = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    fecha_finalizado = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    dotacion_id_finalizado = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    falsa_alarma = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    tipo_dispositivo_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    codigo_dispositivo = sqlalchemy.Column(sqlalchemy.String, index=True)
    modo_safe = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    comuna_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    activo = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    json = sqlalchemy.Column(sqlalchemy.String, index=True)
    fecha_corta_corriente = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    dotacion_id_corta_corriente = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    obtener_imagen = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    obtener_audio = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    transcripion_audio = sqlalchemy.Column(sqlalchemy.String, index=True)
    clasificacion_sentimiento_positivo = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    clasificacion_sentimiento_negativo = sqlalchemy.Column(sqlalchemy.Integer, index=True)

    class Config:
        orm_mode = True
    
class AlarmaCreate(BaseModel):
    dotacion_id: int
    fecha_registro: Optional[datetime]
    fecha_persecucion: Optional[datetime]
    dotacion_id_persecucion: int
    fecha_finalizado: Optional[datetime]
    dotacion_id_finalizado: Optional[int]
    falsa_alarma: Optional[int]
    tipo_dispositivo_id: Optional[int]
    codigo_dispositivo: Optional[str]
    modo_safe: Optional[int]
    comuna_id: Optional[int]
    activo: Optional[int]
    json: Optional[str]
    fecha_corta_corriente: Optional[datetime]
    dotacion_id_corta_corriente: Optional[int]
    obtener_imagen: Optional[int]
    obtener_audio: Optional[int]
    transcripion_audio: Optional[str]
    clasificacion_sentimiento_positivo: Optional[int]
    clasificacion_sentimiento_negativo: Optional[int]

    class Config:
        orm_mode = True

class AlarmaUpdate(BaseModel):
    id: int
    dotacion_id: Optional[int] = None
    fecha_registro: Optional[datetime] = None
    fecha_persecucion: Optional[datetime] = None
    dotacion_id_persecucion: Optional[int] = None
    fecha_finalizado: Optional[datetime] = None
    dotacion_id_finalizado: Optional[int] = None
    falsa_alarma: Optional[int] = None
    tipo_dispositivo_id: Optional[int] = None
    codigo_dispositivo: Optional[str] = None
    modo_safe: Optional[int] = None
    comuna_id: Optional[int] = None
    activo: Optional[int] = None
    json: Optional[str] = None
    fecha_corta_corriente: Optional[datetime] = None
    dotacion_id_corta_corriente: Optional[int] = None
    obtener_imagen: Optional[int] = None
    obtener_audio: Optional[int] = None
    transcripion_audio: Optional[str] = None
    clasificacion_sentimiento_positivo: Optional[int] = None
    clasificacion_sentimiento_negativo: Optional[int] = None
    class Config:
        orm_mode = True
        
class AlarmDelete(BaseModel):
    id: Optional[int] = None