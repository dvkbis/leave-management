
from sqlalchemy.orm import Session
from app.models import LeaveBalance, LeaveType

class BalanceService():
    def get_or_add_balance_request(self, session: Session, employee_id: int, leave_type_id: int, year: int):
        balance = session.query(LeaveBalance).filter(
                LeaveBalance.employee_id == employee_id,
                LeaveBalance.leave_type_id == leave_type_id,
                LeaveBalance.year == year).all()
        if balance:
            return balance[0]
        
        leave_type = session.get(LeaveType, leave_type_id)
        if leave_type is None:
            raise ValueError(f"No Leave Type with ID {leave_type_id}")

        balance = LeaveBalance()
        balance.leave_type_id = leave_type_id
        balance.year = year
        balance.employee_id = employee_id
        balance.allocated_days = leave_type.allocated_days
        balance.used_days = 0

        session.add(balance)
        session.commit()
        session.refresh(balance)

        return balance

    def update_allocated_days(self, session: Session, new_allocated_days:int, balance_id: int, manager_id: int):
        balance = session.get(LeaveBalance, balance_id)
        if balance is None:
            raise ValueError(f"No Leave Balance with ID {balance_id}")
        
        if balance.employee.manager_id != manager_id:
            raise ValueError(f"Permission Denied!")
        
        balance.allocated_days = new_allocated_days
        session.commit()
        session.refresh(balance)

        return balance