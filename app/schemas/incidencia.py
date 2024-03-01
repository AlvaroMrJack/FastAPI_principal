from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class IncidenciaBase(BaseModel):
    id: int | None = None
    dotacion_id: int | None = None
    latitud: float | None = None
    longitud: float | None = None
    descripcion: str | None = None
    categoria_alarma_id: int | None = None
    tipo_reporte: str | None = None
    estado_incidencia: int | None = None
    motivo_rechazo: str | None = None
    fecha_creacion: datetime | None = None
    estado_registro: int | None = None
    
class IncidenciaCreate(BaseModel):
    dotacion_id: Optional[int]
    latitud: Optional[float]
    longitud: Optional[float]
    descripcion: Optional[str]
    categoria_alarma_id: Optional[int]
    tipo_reporte: Optional[str]
    estado_incidencia: Optional[int]
    motivo_rechazo: Optional[str]
    fecha_creacion: Optional[datetime]
    estado_registro: Optional[int]

    class Config:
        orm_mode = True

class IncidenciaUpdate(BaseModel):
    id: int
    dotacion_id: Optional[int] = None
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    descripcion: Optional[str] = None
    categoria_alarma_id: Optional[int] = None
    tipo_reporte: Optional[str] = None
    estado_incidencia: Optional[int] = None
    motivo_rechazo: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    estado_registro: Optional[int] = None

    class Config:
        orm_mode = True
        
class IncidenciaDelete(BaseModel):
    id: Optional[int] = None