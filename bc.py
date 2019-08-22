DIGITS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Converter(object):
    def __init__(self, digits = DIGITS):
        # convert the value to a string
        self.value = ''
        # mediary value is decimal
        self.mediary = 0
        # stores the final converted value; will be a string
        self.converted = ''
        # store the default digits
        self.using(digits)

    def number(self, value):
        # convert the value to a string
        valueType = type(value)
        if valueType != str and valueType == list:
            self.value = value.join('')
        else:
            try:
                self.value = str(value)
            except ValueError:
                raise TypeError('Unable to convert the provided value to a string')
            else:
                pass

    def using(self, digits):
        digitType = type(digits)
        if digitType != str and digitType == list:
            digits = digits.join('')
            self._setDigits(digits)
        else:
            try:
                digits = str(digits)
            except ValueError:
                print('Unable to convert the provided digits to a string. Using last saved value.')
            else:
                self._setDigits(digits)
        return self

    def _setDigits(self, digits):
        self.numDigits = len(digits)
        self.digits = digits
        
    def _leastSignificantFirst(self):
        reversedValue = ''
        for char in reversed(self.value):
            reversedValue += char
        return reversedValue

    def fromBase(self, base):
        if type(base) != int:
            try:
                base = int(base, 10)
            except ValueError:
                raise TypeError('The value must be a decimal number, or a string that can be converted into one.')
        if not (2 < base < self.numDigits):
            raise ValueError('The base must be between 2 and ' + str(self.numDigits))
        # reverse the value string
        reversedValue = self._leastSignificantFirst()
        # convert value string to decimal
        val = 0
        for index in range(base):
            digit = reversedValue[index]
            digitIndex = self.digits.find(digit)
            if digitIndex == -1:
                raise ValueError('Unable to find ' + digit + ' in the current list of given digits. Please ensure you only use characters found within the provided digits.')
            val += digitIndex * base**index
        # store converted string as self.
        self.mediary = int(val)
        return self

    def toBase(self, base):
        if type(base) != int:
            raise TypeError('The provided base must be a number')
        if not (2 < base < self.numDigits):
            raise ValueError('The base must be between 2 and ' + str(self.numDigits))
        # make sure mediary is an integer
        # modulo using `base-1` to get each digit (most significant first)
        # convert each digit to appropriate case-sensitive character
        # insert digit into the converted value string