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

        if not self.validate_buttons(buttons):
            raise ValueError('\'buttons\' has an invalid button.')

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

    def get_button_at(self, index):
        if index >= len(self.buttons):
            raise ValueError('\'index\' is greater than the last ' +
            'position of the array ({0} > {1}).'.format(index, len(self.buttons)-1))
        elif index < 0:
            raise ValueError('\'index\' can\'t be lower than 0.')
        else:
            return self.buttons[index]

    def validate_buttons(self, buttons):
        # This function tries to convert a received value to integer.
        # Returns true if it can, false otherwise.
        def can_parse(value):
            try:
                value = int(value)
                return True
            except:
                return False

        # Verify if the instance already has the 'buttons' property.
        # If this is the case, the function is being called from outside
        # this class.
        instance_buttons = getattr(self, 'buttons', None)
        if instance_buttons:
            raise PermissionException('this function shouldn\'t be called '
            + 'outside of the Level class.')

        # Convert string with list of buttons to array of buttons
        buttons = buttons.split(', ')

        for button in buttons:
            # Validate the addition button
            if button.startswith('+'):
                # Discard the operator
                button = button[1:]
                # Verify if the remainder is a number
                if not can_parse(button):
                    return False

            # Validate the multiplication button
            elif button.startswith('x'):
                # Discard the operator
                button = button[1:]
                # Verify if the remainder is a number
                if not can_parse(button):
                    return False
            else:
                # If it's not listed above, it's not a valid button
                return False

        # Returns true only if all buttons were valid
        return True

class PermissionException(Exception):
    pass
