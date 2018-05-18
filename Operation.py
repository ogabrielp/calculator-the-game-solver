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

        # Square
        if operation.startswith('x^'):
            operand = operation[2:]
            if is_numeric(operand):
                return lambda value: int(math.pow(float(value), float(operand)))

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
                # Convert the value to string to be able to use len()
                str_value = str(value)
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
            operands = operation.split('=>')
            if is_numeric(operands[0]) and is_numeric(operands[1]):
                to_replace = operands[0]
                replacer = operands[1]
                return lambda value: int(str(value).replace(to_replace, replacer))

        return None
