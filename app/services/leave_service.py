from app.models import LeaveRequest, Employee, LeaveRequestStatus, LeaveType, LeaveBalance
from app.models.enums import can_transition
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import select, and_, extract
from app.utils.working_days import compute_working_days

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
        ## TODO Check if the leave days submitted are possible
        if request is None:
            raise ValueError(f"No Request with this ID")
        
        if request.employee_id != employee_id:
            raise ValueError(f"Permission Denied!")
        
        if not can_transition(request.status, LeaveRequestStatus.SUBMITTED):
            raise ValueError(f"Cannot change status from {request.status} to {LeaveRequestStatus.SUBMITTED}")
        
        request.requested_at = datetime.now()
        request.status = LeaveRequestStatus.SUBMITTED
        session.commit()
        return request


    def get_pending_requests(self, session: Session, manager_id: int):
        stmt = (
            select(LeaveRequest)
            .join(Employee,
                   and_(
                       Employee.id == LeaveRequest.employee_id,
                       LeaveRequest.status == LeaveRequestStatus.SUBMITTED,
                       Employee.manager_id == manager_id
                       )
                )
            )
        
        return session.execute(stmt).all()
    
    ## Managing your holidays
    def create_request(self, session: Session, leave_request: LeaveRequest, employee_id: int):
        if leave_request.start_date > leave_request.end_date:
            raise ValueError(f"end_date must be on or after start_date") 
        
        leave_type = session.get(LeaveType, leave_request.leave_type_id)
        if leave_type is None:
            raise ValueError(f"No Leave Type with ID {leave_request.leave_type_id}")
        
        request = LeaveRequest(
            employee_id= employee_id,
            start_date= leave_request.start_date,
            end_date = leave_request.end_date,
            reason = leave_request.reason,
            status = LeaveRequestStatus.DRAFT,
            leave_type_id = leave_request.leave_type_id
        )

        session.add(request)
        session.commit()
        session.refresh(request)
        return request
    
    def update_draft_request(self, session: Session, leave_request: LeaveRequest, leave_request_id: int, employee_id: int):
        request = session.get(LeaveRequest, leave_request_id)
        
        if request is None:
            raise ValueError(f"No Request with ID {leave_request_id}")
        if request.employee_id != employee_id:
            raise ValueError(f"Permission Denied!")
        if request.status != LeaveRequestStatus.DRAFT:
            raise ValueError(f"Only draft request can be updated")
        if leave_request.start_date > leave_request.end_date:
            raise ValueError(f"end_date must be on or after start_date")  
               
        leave_type = session.get(LeaveType, leave_request.leave_type_id)
        if leave_type is None:
            raise ValueError(f"No Leave Type with ID {leave_request.leave_type_id}")
                        
        request.start_date = leave_request.start_date
        request.end_date = leave_request.end_date
        request.reason = leave_request.reason
        request.leave_type_id = leave_request.leave_type_id

        session.commit()
        session.refresh(request)

        return request

    ## Only Draft and Submitted request can be removed
    def remove_request(self, session: Session, leave_request_id: int, employee_id: int):
        request = session.get(LeaveRequest, leave_request_id)

        if request is None:
            raise ValueError(f"No request with ID {leave_request_id}")
        if request.employee_id != employee_id:
            raise ValueError(f"Permission Denied!")
        if request.status not in (LeaveRequestStatus.SUBMITTED, LeaveRequestStatus.DRAFT):
            raise ValueError(f"You can only delete draft or submitted request")
                
        session.delete(request)
        session.commit()

        return request