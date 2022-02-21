from fastapi import Depends,HTTPException, FastAPI
from typing import List
from pydantic import EmailStr
from sqlalchemy.orm import Session

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from routes import join_ce, usuarios, empleados, comercios
from models import model
from schemas import schema
from config.db import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app=FastAPI(
    title = "Comercios-Empleados",
    description = "CRUD en FastAPI",

    docs_url='/',
    redoc_url='/redoc' 
    )   

# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Comercios---------------------------------------------------------------------------

@app.get('/comercios', tags=["Comercios"])
def mostrar_comercios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    listar_comercios = comercios.get_comercios(db=db, skip=skip, limit=limit)
    return listar_comercios

@app.post('/agregar_comercio', response_model=schema.ComercioAdd, tags=["Comercios"], dependencies=[Depends(JWTBearer())])
def agregar_comercio(comercio: schema.ComercioAdd, db: Session = Depends(get_db)):
    uuid = comercios.get_comercio_uuid(db=db, uuid=comercio.uuid)
   
    if uuid:
        raise HTTPException(status_code=400, detail=f"Comercio {comercio.uuid} ya existente en la base de datos: {uuid}")
    
    if comercio.nombre == '' and comercio.activo == '' and comercio.email_contacto == '' and comercio.telefono_contacto == '':
        raise HTTPException(status_code=400, detail = "Datos incompletos!")
    
    return comercios.agregar_comercio(db=db, comercio=comercio)

@app.put('/actualizar_comercio', response_model=schema.ComercioUpdate, tags=["Comercios"], dependencies=[Depends(JWTBearer())])
def actualizar_comercio(uuid: str, update_param: schema.ComercioUpdate, db: Session = Depends(get_db)):
    details = comercios.get_comercio_uuid(db=db, uuid=uuid)
    if not details:
        raise HTTPException(status_code=404, detail="No hay datos para actualizar")

    return comercios.actualizar_comercio(db=db, details=update_param, uuid=uuid)

@app.delete('/eliminar_comercio', tags=["Comercios"], dependencies=[Depends(JWTBearer())])
def eliminar_comercio(uuid: str, db: Session = Depends(get_db)):
    details = comercios.get_comercio_uuid(db=db, uuid=uuid)
    if not details:
        raise HTTPException(status_code=404, detail=f"No hay registro para eliminar")

    try:
        comercios.eliminar_comercio(db=db, uuid=uuid)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"No se puede eliminar: {e}")
    return {"Estado de la eliminacion": "Realizada"}


#Empleados---------------------------------------------------------------------------

@app.get('/empleados', tags=["Empleados"])
def mostrar_empleados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    listar_empleados = empleados.get_empleados(db=db, skip=skip, limit=limit)
    return listar_empleados

@app.post('/agregar_empleado', response_model=schema.EmpleadoAdd, tags=["Empleados"], dependencies=[Depends(JWTBearer())])
def agregar_empleado(empleado: schema.EmpleadoAdd, db: Session = Depends(get_db)):
    uuid = empleados.get_empleado_uuid(db=db, uuid=empleado.uuid)
   
    if uuid:
        raise HTTPException(status_code=400, detail=f"Empleado {empleado.uuid} ya existente en la base de datos: {uuid}")
    
    if empleado.nombre == '' and empleado.apellidos and empleado.pin and empleado.activo :
        raise HTTPException(status_code=400, detail = "Datos incompletos!")
    
    return empleados.agregar_empleado(db=db, empleado=empleado)

@app.put('/actualizar_empleado', response_model=schema.EmpleadoUpdate, tags=["Empleados"], dependencies=[Depends(JWTBearer())])
def actualizar_empleado(uuid: str, update_param: schema.EmpleadoUpdate, db: Session = Depends(get_db)):
    details = empleados.get_empleado_uuid(db=db, uuid=uuid)
    if not details:
        raise HTTPException(status_code=404, detail="No hay datos para actualizar")

    return empleados.actualizar_empleado(db=db, details=update_param, uuid=uuid)

@app.delete('/eliminar_empleado', tags=["Empleados"], dependencies=[Depends(JWTBearer())])
def eliminar_empleado(uuid: str, db: Session = Depends(get_db)):
    details = empleados.get_empleado_uuid(db=db, uuid=uuid)
    if not details:
        raise HTTPException(status_code=404, detail=f"No hay registro para eliminar")

    try:
        empleados.eliminar_empleado(db=db, uuid=uuid)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"No se puede eliminar: {e}")
    return {"Estado de la eliminacion": "Realizada"}


#Usuarios---------------------------------------------------------------------------

@app.get('/usuarios', tags=["Usuarios"])
def mostrar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    listar_usuarios = usuarios.get_usuarios(db=db, skip=skip, limit=limit)
    return listar_usuarios

@app.post("/usuarios/registro", tags=["Usuarios"])
def crear_usuario(usuario: schema.Registro,  db: Session = Depends(get_db)):
    email = usuarios.get_usuario_email(db=db, email=usuario.email)
    if email:
        raise HTTPException(status_code=400, detail=f"Email {usuario.email} ya existente en la base de datos: {email}")
    
    
    return usuarios.agregar_usuario(db=db, usuario=usuario), signJWT(usuario.email)

@app.post("/usuarios/login", tags=["Usuarios"])
def usuario_login(usuario: schema.Login, db: Session = Depends(get_db)):
    email = usuarios.get_usuario_email(db=db, email=usuario.email)
    if email:
        return signJWT(usuario.email)
    else:
        return {
            "Error": "Usuario no registrado"
            }
        
@app.put('/usuarios/actualizar_usuario', response_model=schema.UsuarioUpdate, tags=["Usuarios"], dependencies=[Depends(JWTBearer())])
def actualizar_usuario(email: EmailStr, update_param: schema.UsuarioUpdate, db: Session = Depends(get_db)):
    details = usuarios.get_usuario_email(db=db, email=email)
    if not details:
        raise HTTPException(status_code=404, detail="No hay datos para actualizar")

    return usuarios.actualizar_usuario(db=db, details=update_param, email=email)

@app.delete('/usuarios/eliminar_usuario', tags=["Usuarios"], dependencies=[Depends(JWTBearer())])
def eliminar_usuario(email: EmailStr , db: Session = Depends(get_db)):
    details = usuarios.get_usuario_email(db=db, email=email)
    if not details:
        raise HTTPException(status_code=404, detail=f"No hay registro para eliminar")

    try:
        usuarios.eliminar_usuario(db=db, email=email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"No se puede eliminar: {e}")
    return {"Estado de la eliminacion": "Realizada"}

#Relación de tablas---------------------------------------------------------------------------

@app.get('/join', tags=["Relación (Comercios-Empleados)"])
def mostrar_relacion(db: Session = Depends(get_db)):
    listar = join_ce.get_comerciosempleados(db=db)
    return listar