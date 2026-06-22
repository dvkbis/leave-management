from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database.base import Base

class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique= True,
        nullable=False
    )
    hire_date: Mapped[datetime] = mapped_column(
        nullable=False
    )

    manager_id: Mapped[int | None] = mapped_column(
        ForeignKey("employee.id"),
        nullable=True
    )

    manager: Mapped["Employee | None"] = relationship(
        remote_side=[id],
        back_populates="subordinates",
    )

    subordinates: Mapped[list["Employee"]] = relationship(
        back_populates="manager"
    )