from pydantic import EmailStr
from sqlalchemy.orm import Session
from models import model
from schemas import schema
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)


def get_usuario_email(db: Session, email: EmailStr):
    
    return db.query(model.Usuarios).filter(model.Usuarios.email == email).first()


def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
   
    return db.query(model.Usuarios).offset(skip).limit(limit).all()


def agregar_usuario(db: Session, usuario: schema.Registro):
  
    mv_details = model.Usuarios(
        nombre_completo = usuario.nombre_completo,
        email = usuario.email,
        password = f.encrypt(usuario.password.encode('utf-8'))
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Usuarios(**usuario.dict())


def actualizar_usuario(db: Session, email: EmailStr, details: schema.UsuarioUpdate):
    
    db.query(model.Usuarios).filter(model.Usuarios.email == email).update({
        model.Usuarios.nombre_completo : details.nombre_completo,
        model.Usuarios.password : f.encrypt(details.password.encode('utf-8'))}, synchronize_session = False)    
    db.commit()
  
    return db.query(model.Usuarios).filter(model.Usuarios.email == email).first()


def eliminar_usuario(db: Session, email: EmailStr):
    
    try:
        db.query(model.Usuarios).filter(model.Usuarios.email == email).delete(synchronize_session = False)
        db.commit()
    except Exception as e:
        raise Exception(e)