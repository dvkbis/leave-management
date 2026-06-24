from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, ForeignKey, Identity
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import mapped_column, relationship, Mapped
from app.database.base import Base
from .enums import LeaveRequestStatus

if TYPE_CHECKING:
    from app.models.employee import Employee
    from app.models.leave_type import LeaveType

class LeaveRequest(Base):
    __tablename__ = "leave_request"

    id: Mapped[int] = mapped_column(Identity(start=1), primary_key=True)
    start_date: Mapped[datetime] = mapped_column(nullable=False)
    end_date: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[LeaveRequestStatus] = mapped_column(
        SQLEnum(LeaveRequestStatus),
        nullable=False,
        default=LeaveRequestStatus.DRAFT,
    )
    reason: Mapped[str | None] = mapped_column(String(255))
    requested_at: Mapped[datetime | None] = mapped_column()
    decided_at: Mapped[datetime | None]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    decided_by_id: Mapped[int | None] = mapped_column(ForeignKey("employee.id"))
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"), nullable=False)
    leave_type_id: Mapped[int] = mapped_column(ForeignKey("leave_type.id"), nullable=False)

    employee: Mapped["Employee"] = relationship(
        foreign_keys=[employee_id], back_populates="leave_requests" 
    )
    manager: Mapped["Employee | None"] = relationship(
        foreign_keys=[decided_by_id], back_populates="managed_requests"
    )
    leave_type: Mapped["LeaveType"] = relationship()

    def __repr__(self) -> str:
        return (
            f"LeaveRequest("
            f"id={self.id}, "
            f"status={self.status}, "
            f"start_date={self.start_date}, "
            f"end_date={self.end_date}, "
            f"employee_id={self.employee_id}"
            f")"
        )
    
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
