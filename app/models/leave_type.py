from sqlalchemy import String, Boolean, text
from sqlalchemy.orm import mapped_column, Mapped
from app.database.base import Base

class LeaveType(Base):
    __tablename__ = "leave_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(100), 
        unique= True,
        nullable=False
    )
    allocated_days: Mapped[int | None] = mapped_column(nullable=True)
    require_approval: Mapped[bool] = mapped_column(Boolean, default=False, server_default=text("false"), nullable=False)
