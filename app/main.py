from app.models import LeaveRequest
from app.services.balance_service import BalanceService
from app.services.leave_service import LeaveService
from app.database.session import SessionLocal
from datetime import datetime

def main():
    session = SessionLocal()
    leave_service = LeaveService()
    balance_service = BalanceService()

    """APPROVE REQUEST"""
    # print(leave_service.approve_request(session, 1, 2))
    """SUBMIT REQUEST"""
    # leave_service.submit_request(session, 2, 4)
    # leave_request = session.get(LeaveRequest, 1)
    
    # if leave_request:
    #     print(leave_request)
    """PENDING REQUESTS"""
    # result_pending_request = leave_service.get_pending_requests(session, 1)
    # for request in result_pending_request:
    #     print("-", request)
    """CREATE REQUEST"""
    # creating_request = LeaveRequest()
    # creating_request.start_date = datetime(year=2026, month=10, day=10)
    # creating_request.end_date = datetime(year=2026, month=10, day=10)
    # creating_request.leave_type_id = 1
    # new_request = leave_service.create_request(session, creating_request, 4)
    # print(new_request)
    """UPDATE REQUEST"""
    # new_request.end_date = datetime(year=2026, month=10, day=15)
    # new_request.reason = "health problem"
    # creating_request.leave_type_id = 2
    # updated_request = leave_service.update_draft_request(session, new_request, new_request.id, 4)
    # print(updated_request)
    """REFUSE REQUEST"""
    # leave_service.refuse_request(session, 2, 12)

    """GET OR ADD BALANCE"""
    balance = balance_service.get_or_add_balance_request(session,employee_id= 3, leave_type_id=1, year=2025)
    
    """REFRESH BALANCE"""
    leave_service.refresh_balance(session, balance.id)
    print(balance)
if __name__ == "__main__":
    main()