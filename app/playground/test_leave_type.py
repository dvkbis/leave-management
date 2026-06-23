from app.database.session import SessionLocal
from sqlalchemy import delete
from app.models import LeaveType

session = SessionLocal()

leave_type = LeaveType(
    name = "Paid Leave",
    allocated_days = 25,
    require_approval = True
)

session.add(leave_type)
session.commit()

print(leave_type.id)