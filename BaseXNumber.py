from exceptions import ValueError, TypeError

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
                raise ValueError('Digit \'{0}\' in \'value\' is outside of base {1} range.'.format(digit, base))

        if not 2 <= base <= 10:
            raise ValueError('\'base\' must be >= 2 and <= 10.')

        self.value = value
        self.base = base
        self.overflow = overflow

        if not overflow:
            self.MAXIMUM_VALUE = '{0}'.format(self.base-1)*len(value)

    def increaseByOne(self):
        """
        Adds one to the current value of the number.
        #TODO: generalize this function to increase any amount.
        """
        # Transform string in array of integers
        value_array = [int(digit) for digit in self.value]
        # Add one to last position of the number
        value_array[len(self.value)-1] += 1

        # Iterate through the value resetting values greater than the base
        for i in range(len(self.value)-1, -1, -1):
            if value_array[i] >= self.base:
                # If it's not first position of array
                if i > 0:
                    # Reset current position and increase the previous one by 1
                    value_array[i] = 0
                    value_array[i-1] += 1
                else:
                    # If the first position of the array is greater than the base,
                    # the limit for this base and string length has been reached.
                    if self.overflow:
                        # If overflow is enabled, reset the array and prepend
                        # with 1.
                        value_array = [0] * len(self.value)
                        value_array = [1] + value_array
                    else:
                        # If overflow is disabled, set all the positions of
                        # the array to the maximum possible value.
                        value_array = [self.base-1] * len(self.value)

        # Transform digits back to strings so they can be joined
        value_array = [str(digit) for digit in value_array]
        self.value = ''.join(value_array)

    def get_value(self):
        return self.value

    def get_base(self):
        return self.base

    def get_overflow(self):
        return self.overflow

    def get_maximum_value(self):
        if self.overflow:
            return self.MAXIMUM_VALUE
        else:
            raise AttributeError('instances with \'overflow\' set to \'False\' don\'t have the MAXIMUM_VALUE property.')
