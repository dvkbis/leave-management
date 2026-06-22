# Leave Management

## Dependencies
- python
- sqlalchemy
- psycopg2
- alembic
- postgres
- pip install holidays ?

## Database
- Employee (id, first_name, last_name, hire_date, email, manager_id)
- Leave_Request (id, status, start_date, end_date, leave_type, reason, employee, decided_by, decided_at )
 ex: "approved", 10/10/2026 - 18/10/2026, "Congés payés", Null, 23, 2, 06/10/2026
- Leave_type(id, name, allocated_days)
 ex: "Congés payés", 25
- Leave_Balance (id, employee_id, year, leave_type, used_days, allocated_days)
 ex: 23, 2026,  "Congés Payés", 20
- public_holdays (id, holiday_date, name)
 - 

## Use Case
- Employee can see available days 
- Employee can request days off (Leave_Request)
    - There is a limit, you can't exceed that limit
    - There should be warning when another Employee have holiday at this time 
    - There should be a reject when you already have a request at this time
    - Maybe Employee can see requested / approved days off of others employees
- Manager can see the requested days of each employee
    - He can validate/refuse Request

## Functions
- EMPLOYEE SERVICE
    - log in
- LEAVE REQUEST SERVICE
    - get_pending_requests()
    - get_employees_requests()
    - list_recent_request(end_date)
    - list_available_days(start_date, end_date, have_approved_days)
    - [MANAGER] get_leave_request() 
    - approve_leave_request(id, request_id)
    - refuse_leave_request(id, request_id)
    - cancel_leave_request(id, request_id)
    - CRUD
    - status =  (draft, submitted, cancelled, approved, refused)

- LEAVE TYPE SERVICE
    - get_leave_type(year)
    - CRUD
- LEAVE BALANCE
    - used_days -> should be update automaticaly when requested leave are approved
    - [MANAGER] update_allocated_days(employee_id, leave_balance) -> if allocated days of leave_type table need to change with an employee (new employee)
    - CRUD
- PUBLIC HOLIDAYS 
    - generate_public_holidays(year) 

- SERVICE WORKING DAYS 
    - calculate_working_days(start, end)



## ARCHITECTURE (Service layer)
Service Layer separates : 
- Database concerns
- Business concerns
- Presentation concerns
leave_management/

```python
├── models/
│   ├── employee.py
│   ├── leave_request.py
│   ├── leave_type.py
│   └── leave_balance.py
│
├── repositories/
│   ├── employee_repository.py
│   ├── leave_request_repository.py
│   └── leave_balance_repository.py
│
├── services/
│   ├── leave_request_service.py
│   ├── leave_balance_service.py
│   └── employee_service.py
│
├── utils/
│   ├── holidays.py
│   └── date_calculator.py
│
├── database/
│   ├── session.py
│   └── base.py
│
├── tests/
│
└── main.py
```
## Install
- python -m venv .venv
- .venv\Scripts\activate.bat
- install dependencies
```console
    pip install sqlalchemy
    pip install alembic
    pip install psycopg2-binary
    pip install holidays
```
- Save dependencies
```console
pip freeze > requirements.txt
```
- Install everything :
 pip install -r requirements.txt

## Bonus
- Validates Status transitions
```python
ALLOWED_TRANSITIONS = {
    DRAFT: [SUBMITTED, CANCELLED],
    SUBMITTED: [APPROVED, REFUSED, CANCELLED],
}
```
