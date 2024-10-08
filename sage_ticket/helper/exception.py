class InvalidStateException(Exception):
    """Base class for exceptions in this module."""

    pass


class InvalidOpenStateOperation(InvalidStateException):
    def __init__(
        self, message=" SYSTEM_ERROR: Cannot change current state to  Open state"
    ):
        self.message = message
        super().__init__(self.message)


class InvalidNewStateOperation(InvalidStateException):
    def __init__(
        self, message=" SYSTEM_ERROR: Cannot change current state to  New state"
    ):
        self.message = message
        super().__init__(self.message)


class InvalidPendingStateOperation(InvalidStateException):
    def __init__(
        self, message=" SYSTEM_ERROR: Cannot change current state to pending state"
    ):
        self.message = message
        super().__init__(self.message)


class InvalidHoldStateOperation(InvalidStateException):
    def __init__(
        self, message=" SYSTEM_ERROR: Cannot change current state to hold state"
    ):
        self.message = message
        super().__init__(self.message)


class InvalidResolvedStateOperation(InvalidStateException):
    def __init__(
        self, message=" SYSTEM_ERROR: Cannot change current state to resolved state"
    ):
        self.message = message
        super().__init__(self.message)
