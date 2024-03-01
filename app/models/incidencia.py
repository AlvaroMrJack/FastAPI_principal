import sqlalchemy
from database.settings import Base

class Incidencia(Base):
    __tablename__ = "incidencia"
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    dotacion_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    latitud = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    longitud = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    descripcion = sqlalchemy.Column(sqlalchemy.String, index=True)
    categoria_alarma_id = sqlalchemy.Column(sqlalchemy.Integer)
    tipo_reporte = sqlalchemy.Column(sqlalchemy.String, index=True)
    estado_incidencia = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    motivo_rechazo = sqlalchemy.Column(sqlalchemy.String, index=True)
    fecha_creacion = sqlalchemy.Column(sqlalchemy.DateTime, index=True, nullable=False)
    estado_registro = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    
    class Config:
        orm_mode = True
    