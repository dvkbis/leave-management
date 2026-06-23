from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.leave_request import LeaveRequest
    from app.models.leave_balance import LeaveBalance


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hire_date: Mapped[datetime] = mapped_column(nullable=False)

    manager_id: Mapped[int | None] = mapped_column(ForeignKey("employee.id"))

    manager: Mapped["Employee | None"] = relationship(
        remote_side=[id], back_populates="subordinates"
    )
    subordinates: Mapped[list["Employee"]] = relationship(back_populates="manager")

    leave_requests: Mapped[list["LeaveRequest"]] = relationship(
        foreign_keys="LeaveRequest.employee_id",
        back_populates="employee"
    )
    managed_requests: Mapped[list["LeaveRequest"]] = relationship(
        foreign_keys="LeaveRequest.decided_by_id",
        back_populates="manager"
    )

    leave_balance: Mapped[list["LeaveBalance"]] = relationship(
        back_populates="employee"
    )