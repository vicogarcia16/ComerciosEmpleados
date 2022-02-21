from sqlalchemy.orm import Session
from models import model

def get_comerciosempleados(db: Session):
    return db.query(model.Comercio, model.Empleado).filter(model.Comercio.id == model.Empleado.comercio).all()

