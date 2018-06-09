import math

class Operation:
    """
    The class that centralizes operation info.
    """

    @staticmethod
    def get_operation(operation):
        """
        Gets the function representing an operation.

        :param operation: (string) the operation the user wants the function for.
        :return: the lambda function for the operation.
        """

        def is_numeric(value):
            """
            Determines if a string is an integer number.

            :param value: (string) the value to test.
            :return: a boolean informing if it was possible to parse the string.
            """
            try:
                value = int(value)
                return True
            except:
                return False
        
        def get_sign(value):
            """
            Gets the sign of a number.

            :param value: (int) the value to extract the sign of.
            :return: a string, either '-' if value < 0, '' otherwise.
            """
            return '-' if value < 0 else ''

        # Square
        if operation.startswith('x^'):
            # Remove the 'x^' from the string
            operand = operation[2:]
            if is_numeric(operand):
                return lambda value: int(math.pow(float(value), float(operand)))

        # Flip the sign
        elif operation == '+/-':
            return lambda value: int(value*-1)

        # Basic operations
        elif operation.startswith(('+', '-', 'x', '/')):
            # Strip the operator from the operation string
            operator = operation[0]
            operand = operation[1:]
            if is_numeric(operand):
                # If the operand is a numeric string, parse it as an integer
                # and returns the function that represents the operation.
                operand = int(operand)
                operations = {
                    '+': lambda value: value + operand,
                    '-': lambda value: value - operand,
                    'x': lambda value: value * operand,
                    '/': lambda value: float(value) / operand
                }
                return operations[operator]

        # Delete the last character
        elif operation == '<<':
            # Define the function separately as it would be too illegible if
            # declared directly within the lambda call.
            def substr(value):
                # If there's more than one character
                if math.fabs(value) >= 10:
                    # Remove the last one
                    return int(str(value)[:-1])
                else:
                    # Otherwise just return zero (this is the actual behavior
                    # of the Calculator in the game).
                    return 0

            return lambda value: substr(value)

        # Append number to the end
        elif is_numeric(operation):
            # Add the number to the end of the value and convert it to int
            return lambda value: int(str(value) + operation)

        # Replace
        elif '=>' in operation:
            # Fetch operands at both sides of the arrow
            operands = operation.split('=>')
            # If there's more than one arrow
            if len(operands) > 2:
                return None
            # If both operands are numeric
            if is_numeric(operands[0]) and is_numeric(operands[1]):
                # Replace the one on the left
                to_replace = operands[0]
                # With the one on the right
                replacer = operands[1]
                return lambda value: int(str(value).replace(to_replace, replacer))

        # Reverse
        elif operation == 'Reverse':
            def reverse(value):
                # If the value is negative, there's a minus sign that would
                # be at the end of the string after it was reversed.
                sign = get_sign(value)
                # Remove the sign so that when the string is reversed, the
                # result can be parsed to int.
                value = abs(value)
                # Convert the value to string and revert it
                reversed_value = str(value)[::-1]
                # Return as int preppending the minus sign
                return int(sign + reversed_value)

            return reverse

        # Sum
        elif operation == 'SUM':
            def sum(value):
                # Start the sum at 0
                sum = 0
                # If the value is negative, there's a minus sign that would
                # throw an exception when parsed below, so it's necessary to
                # extract the sign.
                sign = get_sign(value)
                # Remove the sign so we are sure that the function will not try
                # to sum a minus sign.
                value = abs(value)
                # For every digit of the number
                for char in str(value):
                    # Increment the sum with its value
                    sum += int(char)
                return int(sign + str(sum))

            return sum
        
        # Shift left
        elif operation == '<Shift':
            def shift_left(value):
                # Get the sign of the number if it's negative
                sign = get_sign(value)
                # Remove the sign so we are sure that regardless of the shifts,
                # the final result certainly will be a parseable string.
                value = abs(value)
                # Store string conversion to prevent function calls further down
                str_value = str(value)
                # Create a substring of str_value without the first character
                remaining = str_value[1:]
                # Get the first character of str_value
                shifted = str_value[0]
                # Append first character to sustring
                final_value = remaining + shifted
                # Prepend the sign to the value
                return int(sign + final_value)
            
            return shift_left

        # Shift right
        elif operation == 'Shift>':
            def shift_right(value):
                # Get the sign of the number if it's negative
                sign = get_sign(value)
                # Remove the sign so we are sure that regardless of the shifts,
                # the final result certainly will be a parseable string.
                value = abs(value)                
                # Store string conversion to prevent function calls further down
                str_value = str(value)
                # Create a substring of str_value without the last character
                remaining = str_value[:-1]
                # Get the last character of str_value
                shifted = str_value[-1]
                # Prepend substring with last character of str_value
                final_value = shifted + remaining
                 # Prepend the sign to the value
                return int(sign + final_value)

            return shift_right

        # Mirror
        elif operation == 'Mirror':
            def mirror(value):
                # Get the sign of the number if it's negative
                sign = get_sign(value)
                # Remove the sign so we are sure that regardless of the mirroring,
                # the final result certainly will be a parseable string.
                value = abs(value)                
                # Store string conversion to prevent function calls further down
                str_value = str(value)
                # Appends the reversed string to the string itself and add the sign
                return int(sign + str_value + str_value[::-1])

            return mirror
            
        return None
