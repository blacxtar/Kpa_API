# app/models.py
from sqlalchemy import Column, String, Date, JSON
from app.database import Base

class WheelSpec(Base):
    __tablename__ = "wheel_specifications"

    formNumber = Column(String, primary_key=True, index=True)
    submittedBy = Column(String, index=True)
    submittedDate = Column(Date)
    fields = Column(JSON)
