from datetime import datetime
from pydantic import BaseModel

class AlarmaBase(BaseModel):
    id: int | None = None
    dotacion_id: int | None = None
    fecha_registro: datetime | None = None
    fecha_persecucion: datetime | None = None
    dotacion_id_persecucion: int | None = None
    fecha_finalizado: datetime | None = None
    dotacion_id_finalizado: int | None = None
    falsa_alarma: int | None = None
    tipo_dispositivo_id: int | None = None
    codigo_dispositivo: str | None = None
    modo_safe: int | None = None
    comuna_id: int | None = None
    activo: int | None = None
    json: str | None = None
    fecha_corta_corriente: datetime | None = None
    dotacion_id_corta_corriente: int | None = None
    obtener_imagen: int | None = None
    obtener_audio: int | None = None
    transcripion_audio: str | None = None
    clasificacion_sentimiento_positivo: int | None = None
    clasificacion_sentimiento_negativo: int | None = None