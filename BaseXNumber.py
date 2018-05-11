class BaseXNumber:
    """
    Defines a number in base X (with x between 2 and 10).
    """

    def __init__(self, value, base, overflow=False):
        """
        Standard constructor.

        Keyword arguments:
        value -- string representing the number itself. Can have
        trailing zeroes - which will be preserved.
        base -- integer between 2 and 10 (both inclusive).
        overflow -- boolean determining what happens if the
        variable reaches the maximum value for the length of
        the passed string. For instance, on increasing '222'
        (base 3) by 1, if overflow is true, the result will be
        '000'. Otherwise, it will be '1000'.
        """

        # Type verifications
        if not isinstance(value, str):
            raise TypeError('\'value\' must be a string.')

        if not isinstance(base, int):
            raise TypeError('\'base\' must be an integer.')

        if not isinstance(overflow, bool):
            raise TypeError('\'overflow\' must be a boolean.')

        # Value verifications
        if len(value) == 0:
            raise ValueError('\'value\' can\'t be an empty string.')

        if not value.isdigit():
            raise ValueError('\'value\' must only contain numbers.')

        for digit in value:
            if int(digit) >= base:
                raise ValueError('digit \'{0}\' in \'value\' is outside of base {1} range.'.format(digit, base))

        if not 2 <= base <= 10:
            raise ValueError('\'base\' must be >= 2 and <= 10.')

        self.value = value
        self.base = base
        self.overflow = overflow

        if not overflow:
            self.MINIMUM_VALUE = '{0}'.format(self.base-1) * len(value)
            self.MAXIMUM_VALUE = '0' * len(value)

    def __add__(self, baseXnumber):
        # Attribute verifications
        if self.base != baseXnumber.base:
            raise AttributeError('the bases of the two numbers being added must ' +
            'be the same.')

        if self.overflow != baseXnumber.overflow:
            raise AttributeError('the \'overflow\' attribute must be the same ' +
            'in both instances.')

        # Transform value of instance in array of integers
        initial_value_array = [int(digit) for digit in self.value]
        # Transform value being added to the instance in array of integers
        added_value_array = [int(digit) for digit in baseXnumber.value]

        # If the value being added is smaller than the value of the instance
        if len(added_value_array) < len(initial_value_array):
            # Pad the value being added with 0s.
            padding = [0] * (len(initial_value_array) - len(added_value_array))
            added_value_array = padding + added_value_array

        # If the initial value is smaller than the value being added
        if len(initial_value_array) < len(added_value_array) and self.overflow:
            # Pad the initial value with zeros.
            # This only happens if overflow is 'True', because if it's false,
            # the length of the original number can't change.
            padding = [0] * (len(added_value_array) - len(initial_value_array))
            initial_value_array = padding + initial_value_array

        # Define the carry for when the result of the sum is greater than the base
        carry = 0
        # Create the results array by adding every position of the arrays above
        result_value_array = [0] * len(initial_value_array)

        # Iterating backwards through the array
        for i in range(len(initial_value_array)-1, -1, -1):
            # Sum both digits at current position and add the carry
            result_value_array[i] = initial_value_array[i] + added_value_array[i] + carry
            # Resets the carry because it's been used already
            carry = 0

            # The snippet below is how addition works, but we are not familiar
            # with this representation, so an example may explain it better.

            # 9 + 8 = 17, and 17 >= 10
            if result_value_array[i] >= self.base:
                # Carry is 1 (17 / 10 = 1, remainder 7)
                carry = result_value_array[i] / self.base
                # Final value for that position is 7 (the remainder)
                result_value_array[i] %= self.base

        if carry > 0:
            if self.overflow:
                # Prepend the array with the carry (in the example above, 1)
                result_value_array = [carry] + result_value_array
            else:
                # Sets the result to the maximum value of the instance
                result_value_array = [int(digit) for digit in self.MAXIMUM_VALUE]

        # Transform digits back to strings so they can be joined
        result_value_array = [str(digit) for digit in result_value_array]
        result_str = ''.join(result_value_array)

        # Creates a new instance with the final value and returns it
        result = BaseXNumber(value=result_str, base=self.base, overflow=self.overflow)
        return result

    def get_value(self):
        return self.value

    def get_base(self):
        return self.base

    def get_overflow(self):
        return self.overflow

    def get_minimum_value(self):
        if self.overflow:
            return self.MINIMUM_VALUE
        else:
            raise AttributeError('instances with \'overflow\' set to \'False\' don\'t have the MINIMUM_VALUE property.')

    def get_maximum_value(self):
        if self.overflow:
            return self.MAXIMUM_VALUE
        else:
            raise AttributeError('instances with \'overflow\' set to \'False\' don\'t have the MAXIMUM_VALUE property.')
