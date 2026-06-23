from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from app.database.base import Base

class LeaveType(Base):
    __tablename__ = "leave_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
    )
    allocated_days: Mapped[int]
    require_approval: Mapped[bool] = mapped_column(nullable=False)
