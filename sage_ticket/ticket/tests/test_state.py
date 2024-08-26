import pytest

from sage_ticket.ticket.design.state import (
    ClosedState,
    HoldState,
    NewState,
    OpenState,
    PendingState,
    TicketState,
)
from sage_ticket.ticket.helper.choice import TicketStateEnum
from sage_ticket.ticket.helper.exceptions import (
    InvalidHoldStateOppertion,
    InvalidNewStateOppertion,
    InvalidOpenStateOppertion,
    InvalidPendingStateOppertion,
    InvalidResolvedStateOppertion,
)


class TestStateTransitions:
    def test_valid_transitions(self):
        ticket = TicketState(NewState())

        # New -> Open
        ticket.set_open()
        assert ticket.show_state() == TicketStateEnum.OPEN

        # Open -> Pending
        ticket.set_pending()
        assert ticket.show_state() == TicketStateEnum.PENDING

        ticket.set_hold()
        assert ticket.show_state() == TicketStateEnum.HOLD

        ticket.set_closed()
        assert ticket.show_state() == TicketStateEnum.CLOSED

    def test_invalid_transitions(self):
        ticket = TicketState(NewState())

        with pytest.raises(InvalidResolvedStateOppertion):
            ticket.set_resolved()

        ticket.set_open()
        with pytest.raises(InvalidNewStateOppertion):
            ticket.set_new()

        ticket.set_pending()
        with pytest.raises(InvalidOpenStateOppertion):
            ticket.set_open()

        ticket.set_hold()
        with pytest.raises(InvalidPendingStateOppertion):
            ticket.set_pending()

        ticket.set_resolved()
        with pytest.raises(InvalidHoldStateOppertion):
            ticket.set_hold()

        ticket.set_closed()
        with pytest.raises(InvalidPendingStateOppertion):
            ticket.set_pending()


class TestStateInitialization:
    def test_initialization_new_state(self):
        ticket = TicketState(NewState())
        assert ticket.show_state() == TicketStateEnum.NEW

    def test_initialization_open_state(self):
        ticket = TicketState(OpenState())
        assert ticket.show_state() == TicketStateEnum.OPEN

    def test_initialization_pending_state(self):
        ticket = TicketState(PendingState())
        assert ticket.show_state() == TicketStateEnum.PENDING

    def test_initialization_hold_state(self):
        ticket = TicketState(HoldState())
        assert ticket.show_state() == TicketStateEnum.HOLD

    def test_initialization_closed_state(self):
        ticket = TicketState(ClosedState())
        assert ticket.show_state() == TicketStateEnum.CLOSED
