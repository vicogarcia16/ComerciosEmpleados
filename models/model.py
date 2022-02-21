from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from config.db import Base
from sqlalchemy_utils import UUIDType, EmailType
import uuid
import datetime


class Comercio(Base):
    __tablename__ = 'comercio'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    uuid = Column(UUIDType(binary=False),index=True, nullable=False)
    nombre = Column(String(100),index=True, nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    email_contacto = Column(EmailType(50), index=True, nullable=True)  
    telefono_contacto = Column(String(15), index=True, nullable=True)
    api_key = Column(UUIDType(binary=False),index=True, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.datetime.now())
    
class Empleado(Base):
    __tablename__ = 'empleado'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    uuid = Column(UUIDType(binary=False),index=True, nullable=False)
    nombre = Column(String(40),index=True, nullable=False)
    apellidos = Column(String(40),index=True, nullable=False)
    pin = Column(String(6),index=True, nullable=False, unique=True)
    comercio = Column(Integer, ForeignKey('comercio.id'), unique=True)
    fecha_creacion = Column(DateTime, default=datetime.datetime.now())
    activo = Column(Boolean, default=True, nullable=False)
    
class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True,index=True, nullable=False)
    nombre_completo = Column(String(255))
    email= Column(EmailType(50))
    password = Column(String(255))