# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def create_wheel_spec(db: Session, spec: schemas.WheelSpecBase):
    db_spec = models.WheelSpec(**spec.dict())
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_wheel_specs(db: Session, formNumber: str, submittedBy: str, submittedDate: str):
    return db.query(models.WheelSpec).filter_by(
        formNumber=formNumber,
        submittedBy=submittedBy,
        submittedDate=submittedDate
    ).all()
