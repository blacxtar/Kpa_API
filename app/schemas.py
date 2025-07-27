from pydantic import BaseModel
from datetime import date
from typing import Dict, List

class WheelSpecBase(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

    class Config:
        orm_mode = True

# Used for POST (single object response)
class WheelSpecSingleResponse(BaseModel):
    success: bool
    message: str
    data: Dict

# Used for GET (list of results)
class WheelSpecListResponse(BaseModel):
    success: bool
    message: str
    data: List[WheelSpecBase]
