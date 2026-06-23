from app.database.session import SessionLocal
from app.models import LeaveBalance

session = SessionLocal()

leave_balance = LeaveBalance(
    year=2026,
    allocated_days=20,
    used_days=10,
    leave_type_id = 1,
    employee_id = 1
)

session.add(leave_balance)
session.commit()

print(leave_balance.id)
