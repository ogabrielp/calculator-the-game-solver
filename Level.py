class Level:
    """
    Defines a level in Calculator: The Game.
    """
    def __init__(self, index, moves, goal, start, buttons):
        """
        Level constructor.

        Keyword arguments:
        index -- the number identifying the level in the game.
        Has no actual purpose other than to improve on readability.
        Must be a non-zero positive integer.
        moves -- the amount of moves available on this level.
        Must be a non-zero positive integer.
        goal -- the target number of the level. Must be an integer.
        start -- the initial state of the calculator. Must be an
        integer.
        buttons -- a string with the buttons available on the level,
        separated by ', ' (comma and space). This argument is further
        validated by the function '_validate_buttons()'.
        """

        # Type verifications
        if not isinstance(index, int):
            raise TypeError('\'index\' must be an integer.')
        if not isinstance(moves, int):
            raise TypeError('\'moves\' must be an integer.')
        if not isinstance(goal, int):
            raise TypeError('\'goal\' must be an integer.')
        if not isinstance(start, int):
            raise TypeError('\'start\' must be an integer.')
        if not isinstance(buttons, str):
            raise TypeError('\'buttons\' must be a string.')

        # Value verifications
        if index < 1:
            raise ValueError('\'index\' must be a non-zero, positive integer.')
        if moves < 1:
            raise ValueError('\'moves\' must be a non-zero, positive integer.')

        self._validate_buttons(buttons)

        self.index = index
        self.moves = moves
        self.goal = goal
        self.start = start
        self.buttons = buttons.split(', ')

    def get_index(self):
        return self.index

    def get_moves(self):
        return self.moves

    def get_goal(self):
        return self.goal

    def get_start(self):
        return self.start

    def get_buttons(self):
        return self.buttons

    def _validate_buttons(self, buttons):
        return
