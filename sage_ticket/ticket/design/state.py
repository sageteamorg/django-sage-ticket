import abc

from sage_ticket.ticket.helper.choice import TicketStateEnum
from sage_ticket.ticket.helper.exceptions import (
    InvalidHoldStateOppertion,
    InvalidNewStateOppertion,
    InvalidOpenStateOppertion,
    InvalidPendingStateOppertion,
    InvalidResolvedStateOppertion,
)


class State(abc.ABC):
    """Abstract base class representing the state of a ticket in a state
    machine.

    This class defines the interface for different states and provides a way
    to set the current ticket attribute. Each concrete state class must
    implement the abstract methods to handle state-specific behavior.

    Attributes:
        _current_ticket (TicketState): Holds the reference to the ticket's
        current state.

    Methods:
        set_ticket_attribute(ticket): Sets the current ticket reference.
        new(): Abstract method for handling the transition to the 'new' state.
        open(): Abstract method for handling the transition to the 'open' state.
        pending(): Abstract method for handling the transition to the 'pending' state.
        hold(): Abstract method for handling the transition to the 'hold' state.
        resolved(): Abstract method for handling the transition to the 'resolved' state.
        closed(): Abstract method for handling the transition to the 'closed' state.

    """

    _current_ticket = None

    def set_ticket_attribute(self, ticket):
        """Sets the ticket attribute to the given ticket instance.

        Args:
            ticket (TicketState): The ticket instance to associate with the state.

        """
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
    """Manages the state of a ticket and provides methods to transition between
    states.

    This class uses the State design pattern to allow different states of a ticket
    to be represented by different classes that share a common interface.

    Attributes:
        _state (State): The current state of the ticket.

    Methods:
        set_state(state): Sets the current state of the ticket.
        set_new(): Transitions the ticket to the 'new' state.
        set_open(): Transitions the ticket to the 'open' state.
        set_pending(): Transitions the ticket to the 'pending' state.
        set_hold(): Transitions the ticket to the 'hold' state.
        set_resolved(): Transitions the ticket to the 'resolved' state.
        set_closed(): Transitions the ticket to the 'closed' state.
        show_state(): Returns the current state by executing the corresponding
        state method.

    """

    _state = None

    def __init__(self, state):
        self.set_state(state)

    def set_state(self, state):
        """Sets the current state of the ticket and updates the state's ticket
        reference.

        Args:
            state (State): The state to set as the current state.

        """
        self._state = state
        self._state.set_ticket_attribute(self)

    def set_new(self):
        """Transitions the ticket to the 'new' state."""
        self._state.new()

    def set_open(self):
        """Transitions the ticket to the 'open' state."""
        self._state.open()

    def set_pending(self):
        """Transitions the ticket to the 'pending' state."""
        self._state.pending()

    def set_hold(self):
        """Transitions the ticket to the 'hold' state."""
        self._state.hold()

    def set_resolved(self):
        """Transitions the ticket to the 'resolved' state."""
        self._state.resolved()

    def set_closed(self):
        """Transitions the ticket to the 'closed' state."""
        self._state.closed()

    def show_state(self):
        """Executes the method corresponding to the current state and returns
        the result.

        This method uses the class name of the current state to determine the
        appropriate method to execute.

        Returns:
            The result of the executed state method.

        """
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
    """Represents the 'new' state of a ticket.

    This class implements the behavior specific to the 'new' state,
    including transitions to other states.

    """

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
    """Represents the 'open' state of a ticket.

    This class implements the behavior specific to the 'open' state,
    including transitions to other states.

    """

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
    """Represents the 'pending' state of a ticket.

    This class implements the behavior specific to the 'pending' state,
    including transitions to other states.

    """

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
    """Represents the 'hold' state of a ticket.

    This class implements the behavior specific to the 'hold' state,
    including transitions to other states.

    """

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
    """Represents the 'resolved' state of a ticket.

    This class implements the behavior specific to the 'resolved' state,
    including transitions to other states.

    """

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
    """Represents the 'closed' state of a ticket.

    This class implements the behavior specific to the 'closed' state,
    including transitions to other states.

    """

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
