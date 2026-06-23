from app.models import LeaveRequest
from app.services.leave_service import LeaveService
from app.database.session import SessionLocal

def main():
    session = SessionLocal()
    leave_service = LeaveService()


    # print(leave_service.approve_request(session, 1, 2))
    
    # leave_service.submit_request(session, 2, 4)
    leave_request = session.get(LeaveRequest, 1)
    
    if leave_request:
        print(leave_request)

if __name__ == "__main__":
    main()