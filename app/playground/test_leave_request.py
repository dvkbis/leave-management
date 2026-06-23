from app.database.session import SessionLocal
from app.models import LeaveRequest, LeaveRequestStatus
from datetime import datetime

sessions = SessionLocal()

leave_request = LeaveRequest(
    start_date = datetime(2026, 8, 23),
    end_date = datetime(2026, 8, 28),
    status = LeaveRequestStatus.SUBMITTED,
    requested_at = datetime.now(),
    employee_id = 1,
    leave_type_id = 1
)

sessions.add(leave_request)
sessions.commit()

print(leave_request.id)