from unittest.mock import Mock

from app.models.enums import LeaveRequestStatus
from app.services.leave_service import LeaveService


def test_approve_request_success():
    # Arrange
    session = Mock()

    employee = Mock()
    employee.manager_id = 10

    request = Mock()
    request.employee = employee
    request.status = LeaveRequestStatus.SUBMITTED

    session.get.return_value = request

    service = LeaveService()
    service.manage_request = Mock()

    # Act
    result = service.approve_request(
        session=session,
        manager_id=10,
        request_id=1,
    )

    # Assert
    assert result == request

    session.get.assert_called_once()
    service.manage_request.assert_called_once_with(
        10,
        request,
        LeaveRequestStatus.APPROVED,
    )
    session.commit.assert_called_once()