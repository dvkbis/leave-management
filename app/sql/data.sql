-- Leave Types
INSERT INTO leave_type (id, name, allocated_days, require_approval)
VALUES
    (1, 'Annual Leave', 25, true),
    (2, 'Sick Leave', 10, false),
    (3, 'Unpaid Leave', NULL, true);


-- Employees
INSERT INTO employee (
    id,
    first_name,
    last_name,
    email,
    hire_date,
    manager_id
)
VALUES
    (1, 'Alice', 'Martin', 'alice.martin@company.com', '2020-01-15', NULL),
    (2, 'Bob', 'Dupont', 'bob.dupont@company.com', '2021-03-10', 1),
    (3, 'Charlie', 'Lambert', 'charlie.lambert@company.com', '2022-06-20', 1),
    (4, 'Diana', 'Peeters', 'diana.peeters@company.com', '2023-02-01', 2);


-- Leave Balances
INSERT INTO leave_balance (
    id,
    year,
    allocated_days,
    used_days,
    leave_type_id,
    employee_id
)
VALUES
    (1, 2025, 25, 5, 1, 2),
    (2, 2025, 25, 10, 1, 3),
    (3, 2025, 25, 2, 1, 4),
    (4, 2025, 10, 3, 2, 2),
    (5, 2025, 10, 1, 2, 3);

-- Leave Requests
INSERT INTO leave_request (
    id,
    start_date,
    end_date,
    status,
    reason,
    requested_at,
    decided_at,
    created_at,
    decided_by_id,
    employee_id,
    leave_type_id
)
VALUES
(
    1,
    '2025-07-01',
    '2025-07-05',
    'APPROVED',
    'Summer vacation',
    '2025-06-01 09:00:00',
    '2025-06-02 14:00:00',
    '2025-06-01 09:00:00',
    1,
    2,
    1
),
(
    2,
    '2025-08-10',
    '2025-08-12',
    'SUBMITTED',
    'Family event',
    '2025-06-15 10:30:00',
    NULL,
    '2025-06-15 10:30:00',
    NULL,
    3,
    1
),
(
    3,
    '2025-06-18',
    '2025-06-19',
    'REFUSED',
    'Personal matters',
    '2025-06-05 08:00:00',
    '2025-06-06 11:15:00',
    '2025-06-05 08:00:00',
    1,
    4,
    1
),
(
    4,
    '2025-06-23',
    '2025-06-24',
    'DRAFT',
    'Medical appointment',
    '2025-06-20 16:00:00',
    NULL,
    '2025-06-20 16:00:00',
    NULL,
    2,
    2
);