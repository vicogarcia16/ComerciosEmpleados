from sqlalchemy.orm import Session
from models import model
from schemas import schema

def get_comercio_uuid(db: Session, uuid: str):
    
    return db.query(model.Comercio).filter(model.Comercio.uuid == uuid).first()


def get_comercios(db: Session, skip: int = 0, limit: int = 100):
   
    return db.query(model.Comercio).offset(skip).limit(limit).all()


def agregar_comercio(db: Session, comercio: schema.ComercioAdd):
  
    mv_details = model.Comercio(
        uuid = comercio.uuid,
        nombre = comercio.nombre,
        activo = comercio.activo,
        email_contacto = comercio.email_contacto,
        telefono_contacto = comercio.telefono_contacto,
        api_key = comercio.api_key
        
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Comercio(**comercio.dict())


def actualizar_comercio(db: Session, uuid: str, details: schema.ComercioUpdate):

    db.query(model.Comercio).filter(model.Comercio.uuid == uuid).update(vars(details))
    db.commit()
    return db.query(model.Comercio).filter(model.Comercio.uuid == uuid).first()


def eliminar_comercio(db: Session, uuid: str):
    
    try:
        db.query(model.Comercio).filter(model.Comercio.uuid == uuid).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)