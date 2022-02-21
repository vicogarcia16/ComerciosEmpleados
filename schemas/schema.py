from typing import Optional
from pydantic import BaseModel,Field, EmailStr
from uuid import UUID

import uuid as _uuid

#Empleados---------------------------------------------------------------------------

class Empleado(BaseModel):
    id: Optional[int]
    nombre: str
    apellidos: str
    comercio: int
    activo: bool

    
class EmpleadoAdd(Empleado):
    uuid: UUID = Field(default = _uuid.uuid4())
    pin:str

    class Config:
        orm_mode = True

class EmpleadoUpdate(BaseModel):
    nombre: str
    apellidos: str
    pin:str
    activo: bool

    class Config:
        orm_mode = True
        
#Comercios---------------------------------------------------------------------------

class Comercio(BaseModel):
    id: Optional[int]
    nombre: str
    activo: bool
    email_contacto: EmailStr
    telefono_contacto: str

    
class ComercioAdd(Comercio):
    uuid: UUID = Field(default = _uuid.uuid4())
    api_key: UUID = Field(default = _uuid.uuid4())

    class Config:
        orm_mode = True

class ComercioUpdate(BaseModel):
    nombre: str
    activo: bool
    email_contacto: EmailStr
    telefono_contacto: str

    class Config:
        orm_mode = True        
        
#Usuarios---------------------------------------------------------------------------

class Registro(BaseModel):
    nombre_completo: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        orm_mode = True
        schema_extra = {
            "Ejemplo": {
                "nombre_completo": "Víctor Manuel García Negrete",
                "email": "mg_619@hotmail.com",
                "password": "password"
            }
        }

class Login(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        orm_mode = True
        schema_extra = {
            "Ejemplo": {
                "email": "mg_619@hotmail.com",
                "password": "password"
            }
        }
    
class UsuarioUpdate(BaseModel):
    nombre_completo: str = Field(...)
    password: str = Field(...)
    class Config:
        orm_mode = True
        
        