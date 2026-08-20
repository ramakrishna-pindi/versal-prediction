from datetime import datetime
from sqlalchemy import Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database.base import Base

class Prediction(Base):
    __tablename__ = "predictions"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    previous_units: Mapped[float] = mapped_column(Float)
    current_units: Mapped[float] = mapped_column(Float)
    people: Mapped[int] = mapped_column(Integer)
    acs: Mapped[int] = mapped_column(Integer)
    fans: Mapped[int] = mapped_column(Integer)
    fridges: Mapped[int] = mapped_column(Integer)
    tvs: Mapped[int] = mapped_column(Integer)
    month: Mapped[int] = mapped_column(Integer)
    predicted_bill: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="predictions")
