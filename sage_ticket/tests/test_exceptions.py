import pytest

from sage_ticket.design.state import (
    HoldState,
    NewState,
    OpenState,
    PendingState,
    ResolvedState,
    TicketState,
)
from sage_ticket.helper.exception import (
    InvalidHoldStateOperation ,
    InvalidNewStateOperation ,
    InvalidOpenStateOperation ,
    InvalidPendingStateOperation ,
    InvalidResolvedStateOperation ,
    InvalidStateException,
)


class TestStateExceptions:
    def test_invalid_new_state_operation(self):
        ticket = TicketState(OpenState())
        with pytest.raises(InvalidNewStateOperation ) as excinfo:
            ticket.set_new()
        assert (
            str(excinfo.value)
            == " SYSTEM_ERROR: Cannot change current state to  New state"
        )

    def test_invalid_open_state_operation(self):
        ticket = TicketState(PendingState())
        with pytest.raises(InvalidOpenStateOperation ) as excinfo:
            ticket.set_open()
        assert (
            str(excinfo.value)
            == " SYSTEM_ERROR: Cannot change current state to  Open state"
        )

    def test_invalid_pending_state_operation(self):
        ticket = TicketState(HoldState())
        with pytest.raises(InvalidPendingStateOperation ) as excinfo:
            ticket.set_pending()
        assert (
            str(excinfo.value)
            == " SYSTEM_ERROR: Cannot change current state to pending state"
        )

    def test_invalid_hold_state_operation(self):
        ticket = TicketState(ResolvedState())
        with pytest.raises(InvalidHoldStateOperation ) as excinfo:
            ticket.set_hold()
        assert (
            str(excinfo.value)
            == " SYSTEM_ERROR: Cannot change current state to hold state"
        )

    def test_invalid_resolved_state_operation(self):
        ticket = TicketState(NewState())
        with pytest.raises(InvalidResolvedStateOperation ) as excinfo:
            ticket.set_resolved()
        assert (
            str(excinfo.value)
            == " SYSTEM_ERROR: Cannot change current state to resolved state"
        )

    def test_base_invalid_state_exception(self):
        with pytest.raises(InvalidStateException):
            raise InvalidStateException("This is a base exception test")
