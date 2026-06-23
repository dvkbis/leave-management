from datetime import datetime

from app.database.session import SessionLocal
from app.models import Employee

session = SessionLocal()

employee = Employee(
    first_name="John",
    last_name="Doe",
    email="john.doe@test.com",
    hire_date=datetime.now(),
)

session.add(employee)
session.commit()

print(employee.id)