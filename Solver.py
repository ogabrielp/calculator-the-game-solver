from BaseXNumber import BaseXNumber
from Level import Level
from Calculator import Calculator

import math

#TODO discard sequences where one of the actions produces no effect

class Solver:
    """
    The class that wraps it all.
    """

    def solve(self, level):
        """
        Static function that solves a particular level.

        Keyword arguments:
        level -- instance of Level that is going to be solved.
        """

        # Type verifications
        if not isinstance(level, Level):
            raise TypeError('\'level\' must be an instance of Level.')

        # Every solution can be represented as a base X number of length Y,
        # where X is the amount of buttons and Y is the amount of moves.
        # The numbers between [0, X-1] each represent a button, and the string
        # of numbers mean the sequence in which they're called.

        # On level 2, you have buttons +2 and +3, which can be mapped to the
        # digits 0 and 1, respectively. Since you have 3 moves, the length
        # of the string representing the solution has 3 digits, each
        # representing a button. 011, for instance, represents pressing +2,
        # then +3, and finally, +3 again.

        # Initialize the counter with Y zeroes, where Y is the amount of
        # moves for this particular level.
        counter_initial_value = '0'*level.get_moves()
        # Set the base to the amount of buttons
        counter_base = len(level.get_buttons())
        # Initialize the counter with the variables defined above
        counter = BaseXNumber(value=counter_initial_value, base=counter_base)

        # Initialize the calculator for the solution
        calculator = Calculator(level)

        # Define the instance's properties with the values defined above
        self.calculator = calculator
        self.counter = counter

        # Try the first possible sequence (a string of zeroes)
        if self.sequence_works(counter.value):
            return self.counter_to_buttons(counter.value)
        else:
            # Since overflow for the counter is False, when it reaches
            # the maximum value and adds 1 again, it will remain the same.
            # That's the stopping condition.
            while counter + 1 != counter:
                # Try the current sequence
                if self.sequence_works(counter.value):
                    return self.counter_to_buttons(counter.value)
                # If it didn't work, increase the counter by 1
                counter += '1'

    def sequence_works(self, sequence):
        """
        Tries a particular sequence of operations.
        """
        # Reset the calculator to the original state
        self.calculator.clear()
        # Convert the sequence to array of integers
        sequence = [int(digit) for digit in sequence]
        # Get the level from the instance's calculator
        level = self.calculator.get_level()

        # Iterate throught the values of the array above
        for digit in sequence:
            # Map the digit to its corresponding button
            button = level.get_button_at(digit)
            # Perform the operation defined by the button
            self.calculator.perform_operation(button)
            # Create an alias for 'current_value' to reduce the length
            # of the if line below.
            current_value = self.calculator.get_current_value()
            # If the number has a non-zero decimal part, it doesn't work,
            # as there are no levels where the goal is a decimal number.
            if math.fabs(int(current_value)) < math.fabs(current_value):
                return False

        # If the sequence successfully arrived at the desired result
        if self.calculator.get_current_value() == level.get_goal():
            return True
        else:
            return False

    def counter_to_buttons(self, sequence):
        # Convert the string to array of digits
        sequence = [int(digit) for digit in sequence]
        # Get the level from the instance's calculator
        level = self.calculator.get_level()
        # Initialize the array that will be filled with the list of buttons
        # used in the solution.
        buttons = []

        for digit in sequence:
            # Map the digit to the corresponding button and add it to the
            # buttons array.
            buttons.append(level.get_button_at(digit))

        # Join the array with arrows and return the string.
        return ' => '.join(buttons)
