from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import TYPE_CHECKING
from app.database.base import Base


if TYPE_CHECKING:
    from app.models.employee import Employee
    from app.models.leave_type import LeaveType 
       
class LeaveBalance(Base):
    __tablename__ = "leave_balance"

    id: Mapped[int] = mapped_column(primary_key= True)
    year: Mapped[int] = mapped_column(nullable= False)
    allocated_days: Mapped[int | None]
    used_days: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        server_default="0"
    )

    leave_type_id: Mapped[int] = mapped_column(
        ForeignKey("leave_type.id"),
        nullable= False
    )
    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employee.id"),
        nullable= False
    )

    employee: Mapped["Employee"] = relationship(
        back_populates="leave_balance"
    )
    leave_type: Mapped["LeaveType"] = relationship()