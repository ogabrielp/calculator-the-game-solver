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

        # Basic operations
        if operation.startswith(('+', '-', 'x', '/')):
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
            return None

        return None
