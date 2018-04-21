from Level import Level

class Calculator:
    """
    Defines the main class to be used by the solver.
    Represents the actual calculator inside Calculator: The Game.
    """
    def __init__(self, level=None):
        """
        Calculator constructor.

        Keyword arguments:
        level -- (optional) instance of Level describing the current level.
        """

        # Type verifications
        if level and not isinstance(level, Level):
            raise TypeError('\'level\' must be an instance of Level.')

        self.level = level
        self.current_value = level.start if level else None

    def perform_operation(self, operation):
        """
        Performs the given operation over the current value of the calculator.

        Keyword arguments:
        operation -- string representing the operation.
        """

        return

    def set_level(self, level):
        """
        Restarts the instance, setting the current level of the calculator.

        Keyword arguments:
        level -- instance of Level describing the current level.
        """
        self.__init__(level)

    def get_current_value(self):
        return self.current_value
