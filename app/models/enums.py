from enum import Enum

class LeaveRequestStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    CANCELLED = "cancelled"
    APPROVED = "approved"
    REFUSED = "refused"

ALLOWED_TRANSITIONS = {
    LeaveRequestStatus.DRAFT: {
        LeaveRequestStatus.SUBMITTED,
        LeaveRequestStatus.CANCELLED,
    },
    LeaveRequestStatus.SUBMITTED: {
        LeaveRequestStatus.APPROVED,
        LeaveRequestStatus.REFUSED,
        LeaveRequestStatus.CANCELLED,
    },
    LeaveRequestStatus.APPROVED: set(),
    LeaveRequestStatus.REFUSED: set(),
    LeaveRequestStatus.CANCELLED: set(),
}

def can_transition(current: LeaveRequestStatus, new: LeaveRequestStatus) -> bool:
    return new in ALLOWED_TRANSITIONS.get(current, set())