# app/routers/wheel_spec.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/forms/wheel-specifications", response_model=schemas.WheelSpecSingleResponse)
def submit_wheel_spec(spec: schemas.WheelSpecBase, db: Session = Depends(get_db)):
    result = crud.create_wheel_spec(db, spec)
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": result.formNumber,
            "submittedBy": result.submittedBy,
            "submittedDate": result.submittedDate,
            "status": "Saved"
        }
    }

@router.get("/api/forms/wheel-specifications", response_model=schemas.WheelSpecListResponse)
def get_spec(formNumber: str, submittedBy: str, submittedDate: str, db: Session = Depends(get_db)):
    data = crud.get_wheel_specs(db, formNumber, submittedBy, submittedDate)
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": data
    }
