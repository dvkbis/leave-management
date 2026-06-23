from app.models import LeaveRequest, Employee, LeaveRequestStatus
from app.models.enums import can_transition
from sqlalchemy.orm import Session
from datetime import datetime

class LeaveService():

    def approve_request(self, session: Session, manager_id: int, request_id: int):
        request = session.get(LeaveRequest, request_id)
        if request is None:
            raise ValueError(f"No Request with this ID")
        
        if request.employee.manager_id != manager_id:
            raise ValueError(f"Permission Denied!")
                  
        if can_transition(request.status, LeaveRequestStatus.APPROVED) == False:
            raise ValueError(f"Cannot change status from {request.status} to {LeaveRequestStatus.APPROVED}")
        
        self.manage_request(manager_id, request, LeaveRequestStatus.APPROVED)
        session.commit()

        return request

    def refuse_request(self, session: Session, manager_id: int, request_id: int):
        request = session.get(LeaveRequest, request_id)
        if request is None:
            raise ValueError(f"No Request with this ID")
        
        if request.employee.manager_id != manager_id:
            raise ValueError(f"Permission Denied!")
                  
        if can_transition(request.status, LeaveRequestStatus.REFUSED) == False:
            raise ValueError(f"Cannot change status from {request.status} to {LeaveRequestStatus.REFUSED}")
        
        self.manage_request(manager_id, request, LeaveRequestStatus.REFUSED)
        session.commit()
        return request

    def cancel_request(self, session: Session, manager_id: int, request_id: int):
        request = session.get(LeaveRequest, request_id)
        if request is None:
            raise ValueError(f"No Request with this ID")
        
        if request.employee.manager_id != manager_id:
            raise ValueError(f"Permission Denied!")
                  
        if can_transition(request.status, LeaveRequestStatus.CANCELLED) == False:
            raise ValueError(f"Cannot change status from {request.status} to {LeaveRequestStatus.CANCELLED}")
        
        self.manage_request(manager_id, request, LeaveRequestStatus.CANCELLED)
        session.commit()
        return request

    def manage_request(self, manager_id: int, request: LeaveRequest, new_statut: LeaveRequestStatus):
        request.decided_by_id = manager_id
        request.decided_at = datetime.now()
        request.status = new_statut

    def submit_request(self, session: Session, employee_id: int, request_id: int):
        request = session.get(LeaveRequest, request_id)
        
        if request is None:
            raise ValueError(f"No Request with this ID")
        
        if request.employee_id != employee_id:
            raise ValueError(f"Permission Denied!")
        
        if not can_transition(request.status, LeaveRequestStatus.SUBMITTED):
            raise ValueError(f"Cannot change status from {request.status} to {LeaveRequestStatus.SUBMITTED}")
        
        request.requested_at = datetime.now()
        request.status = LeaveRequestStatus.SUBMITTED
