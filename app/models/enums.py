from enum import Enum

class LeaveRequestStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    CANCELLED = "cancelled"
    APPROVED = "approved"
    REFUSED = "refused"