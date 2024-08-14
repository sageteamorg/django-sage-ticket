import abc

from django_sage_ticket.ticket.helper.choice import TicketStateEnum
from django_sage_ticket.ticket.helper.exceptions import (
    InvalidHoldStateOppertion,
    InvalidNewStateOppertion,
    InvalidOpenStateOppertion,
    InvalidPendingStateOppertion,
    InvalidResolvedStateOppertion,
)


class State(abc.ABC):
    _current_ticket = None

    def set_ticket_attribute(self, ticket):
        self._current_ticket = ticket

    @abc.abstractmethod
    def new(self):
        raise NotImplementedError

    @abc.abstractmethod
    def open(self):
        raise NotImplementedError

    @abc.abstractmethod
    def pending(self):
        raise NotImplementedError

    @abc.abstractmethod
    def hold(self):
        raise NotImplementedError

    @abc.abstractmethod
    def resolved(self):
        raise NotImplementedError

    @abc.abstractmethod
    def closed(self):
        raise NotImplementedError


class TicketState:
    _state = None

    def __init__(self, state):
        self.set_state(state)

    def set_state(self, state):
        self._state = state
        self._state.set_ticket_attribute(self)

    def set_new(self):
        self._state.new()

    def set_open(self):
        self._state.open()

    def set_pending(self):
        self._state.pending()

    def set_hold(self):
        self._state.hold()

    def set_resolved(self):
        self._state.resolved()

    def set_closed(self):
        self._state.closed()

    def show_state(self):
        """Using the name of the current state class, it obtains the dictionary
        key and executes the same state and returns the output."""
        state_map = {
            "NewState": self._state.new,
            "OpenState": self._state.open,
            "PendingState": self._state.pending,
            "HoldState": self._state.hold,
            "ResolvedState": self._state.resolved,
            "ClosedState": self._state.closed,
        }
        show_current_state = state_map.get(self._state.__class__.__name__)

        return show_current_state()


class NewState(State):
    def new(self):
        return TicketStateEnum.NEW

    def open(self):
        return self._current_ticket.set_state(OpenState())

    def pending(self):
        raise InvalidPendingStateOppertion()

    def hold(self):
        raise InvalidHoldStateOppertion()

    def resolved(self):
        raise InvalidResolvedStateOppertion()

    def closed(self):
        return self._current_ticket.set_state(ClosedState())


class OpenState(State):
    def new(self):
        raise InvalidNewStateOppertion()

    def open(self):
        return TicketStateEnum.OPEN

    def pending(self):
        return self._current_ticket.set_state(PendingState())

    def hold(self):
        raise InvalidHoldStateOppertion()

    def resolved(self):
        raise InvalidResolvedStateOppertion()

    def closed(self):
        return self._current_ticket.set_state(ClosedState())


class PendingState(State):
    def new(self):
        raise InvalidNewStateOppertion()

    def open(self):
        raise InvalidOpenStateOppertion()

    def pending(self):
        return TicketStateEnum.PENDING

    def hold(self):
        return self._current_ticket.set_state(HoldState())

    def resolved(self):
        raise InvalidResolvedStateOppertion()

    def closed(self):
        return self._current_ticket.set_state(ClosedState())


class HoldState(State):
    def new(self):
        raise InvalidNewStateOppertion()

    def open(self):
        raise InvalidOpenStateOppertion()

    def pending(self):
        raise InvalidPendingStateOppertion()

    def hold(self):
        return TicketStateEnum.HOLD

    def resolved(self):
        return self._current_ticket.set_state(ReslovedState())

    def closed(self):
        return self._current_ticket.set_state(ClosedState())


class ReslovedState(State):
    def new(self):
        raise InvalidNewStateOppertion()

    def open(self):
        raise InvalidOpenStateOppertion

    def pending(self):
        raise InvalidPendingStateOppertion

    def hold(self):
        raise InvalidHoldStateOppertion

    def resolved(self):
        return TicketStateEnum.RESOLVED

    def closed(self):
        return self._current_ticket.set_state(ClosedState())


class ClosedState(State):
    def new(self):
        raise InvalidNewStateOppertion()

    def open(self):
        return self._current_ticket.set_state(OpenState())

    def pending(self):
        raise InvalidPendingStateOppertion()

    def hold(self):
        raise InvalidHoldStateOppertion()

    def resolved(self):
        raise InvalidResolvedStateOppertion()

    def closed(self):
        return TicketStateEnum.CLOSED


state = TicketState(OpenState())

state.set_pending()

print(state.show_state())
