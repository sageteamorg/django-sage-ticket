class InvalidStateException(Exception):
    """Base class for exceptions in this module."""

    pass


class InvalidOpenStateOppertion(InvalidStateException):
    def __init__(
        self, messsage=" SYSTEM_ERROR: Cannot change current state to  Open state"
    ):
        self.message = messsage
        super().__init__(self.message)


class InvalidNewStateOppertion(InvalidStateException):
    def __init__(
        self, messsage=" SYSTEM_ERROR: Cannot change current state to  New state"
    ):
        self.message = messsage
        super().__init__(self.message)


class InvalidPendingStateOppertion(InvalidStateException):
    def __init__(
        self, messsage=" SYSTEM_ERROR: Cannot change current state to pending state"
    ):
        self.message = messsage
        super().__init__(self.message)


class InvalidHoldStateOppertion(InvalidStateException):
    def __init__(
        self, messsage=" SYSTEM_ERROR: Cannot change current state to hold state"
    ):
        self.message = messsage
        super().__init__(self.message)


class InvalidResolvedStateOppertion(InvalidStateException):
    def __init__(
        self, messsage=" SYSTEM_ERROR: Cannot change current state to resolved state"
    ):
        self.message = messsage
        super().__init__(self.message)
