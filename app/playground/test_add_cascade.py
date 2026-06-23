from app.database.session import SessionLocal
from app.models import LeaveBalance, LeaveType, Employee
from datetime import datetime

session = SessionLocal()

leave_type = LeaveType(
    name = "Sick Leave",
    require_approval = False
)

employee = Employee(
    first_name="Sacha",
    last_name="Doe",
    email="sacha.doe@test.com",
    hire_date=datetime.now(),
)

leave_balance = LeaveBalance(
    year=2026,
    used_days=10,
    leave_type = leave_type,
    employee = employee
)

session.add(leave_balance)
session.commit()

print(leave_balance.id)
