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
        self.previous_value = level.start if level else None

    def perform_operation(self, operation):
        """
        Performs the given operation over the current value of the calculator.

        Keyword arguments:
        operation -- string representing the operation.
        """

        # Store current value as the previous value since the current value
        # is going to be changed in the following lines.
        self.previous_value = self.current_value

        # Addition
        if operation.startswith('+'):
            # Strip the operator from the operation string
            operand = operation.replace('+', '')
            self.current_value += int(operand)

        return

    def set_level(self, level):
        """
        Restarts the instance, setting the current level of the calculator.

        Keyword arguments:
        level -- instance of Level describing the current level.
        """
        self.__init__(level)

    def get_previous_value(self):
        return self.previous_value

    def get_current_value(self):
        return self.current_value

    def get_level(self):
        return self.level

    def clear(self):
        """
        An alias to the __init__ function to improve code legibility.
        """
        self.__init__(self.level)
