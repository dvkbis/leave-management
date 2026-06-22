from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from datetime import datetime
from app.database.base import Base
from app.models.employee import Employee
from app.models.leave_type import LeaveType

class LeaveRequest(Base):
    __tablename__ = "leave_request"
    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[datetime] = mapped_column(
        nullable=False
    )
    end_date: Mapped[datetime] = mapped_column(
        nullable=False
    )
    status: Mapped[str] = mapped_column(String(20), nullable= False)
    # status = Column(Enum("DRAFT", "SUBMITTED", "CANCELLED", "APPROVED", "REFUSED", name= "leave_request_state", native_enum= "False"), nullable= False)
    reason: Mapped[str] = mapped_column(String(255))
    decided_at: Mapped[datetime]

    decided_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("employee.id")
    )
    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employee.id"), 
        nullable=False
    )
    leave_type_id: Mapped[int] = mapped_column(
        ForeignKey("leave_type.id"), 
        nullable=False
    )
    
    manager: Mapped["Employee | None"] = relationship(back_populates="managed_requests")
    employee: Mapped["Employee"] = relationship(back_populates="leave_requests")
    leave_type: Mapped["LeaveType"] = relationship()
