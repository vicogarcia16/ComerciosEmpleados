from sqlalchemy.orm import Session
from models import model
from schemas import schema

def get_empleado_uuid(db: Session, uuid: str):
    
    return db.query(model.Empleado).filter(model.Empleado.uuid == uuid).first()


def get_empleados(db: Session, skip: int = 0, limit: int = 100):
   
    return db.query(model.Empleado).offset(skip).limit(limit).all()


def agregar_empleado(db: Session, empleado: schema.EmpleadoAdd):
  
    mv_details = model.Empleado(
        uuid = empleado.uuid,
        nombre = empleado.nombre,
        apellidos = empleado.apellidos,
        pin=empleado.pin,
        comercio= empleado.comercio,
        activo = empleado.activo
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Empleado(**empleado.dict())


def actualizar_empleado(db: Session, uuid: str, details: schema.EmpleadoUpdate):

    db.query(model.Empleado).filter(model.Empleado.uuid == uuid).update(vars(details))
    db.commit()
    return db.query(model.Empleado).filter(model.Empleado.uuid == uuid).first()


def eliminar_empleado(db: Session, uuid: str):
    
    try:
        db.query(model.Empleado).filter(model.Empleado.uuid == uuid).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)