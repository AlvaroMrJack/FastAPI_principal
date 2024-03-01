

from pydantic import BaseModel


class GeneralResponse(BaseModel):
    estado: str | None = None
    icono: str | None = None
    validacion: str | None = None
    mensaje: str | None = None
    dotacion_id: int | None = None
    dotacion_usuario: int | None = None
    token_firebase: str | None = None
    
    