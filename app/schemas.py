# app/schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Dict,List

class WheelSpecBase(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

class WheelSpecResponse(BaseModel):
    success: bool
    message: str
    data: List[WheelSpecBase]
