class RomanNumber:
    _values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    _numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                 (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                 (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def __init__(self, value):
        self.rom_value = self.int_value = None
        if isinstance(value, str) and self.is_roman(value):
            self.rom_value = value
            self.int_value = self.decimal_number()
        elif isinstance(value, int) and self.is_int(value):
            self.int_value = value
            self.rom_value = self.roman_number()
        else:
            print('ошибка')

    def decimal_number(self):
        if not self.rom_value:
            return None
        return sum(self._values[c] * (1 if self._values[c] >= self._values.get(n, 0) else -1)
                  for c, n in zip(self.rom_value, self.rom_value[1:] + 'I'))

    def roman_number(self):
        if not self.int_value:
            return None
        num, result = self.int_value, ''
        for val, sym in self._numerals:
            result += sym * (num // val)
            num %= val
        return result

    def __str__(self):
        return self.rom_value or 'None'

    __repr__ = __str__

    def _get_val(self, other):
        return other.int_value if isinstance(other, RomanNumber) else other

    def _operation(self, other, op):
        if self.int_value is None:
            return RomanNumber._null()
        other_val = self._get_val(other)
        if other_val is None:
            return RomanNumber._null()
        result = op(self.int_value, other_val)
        if not self.is_int(result):
            print('ошибка')
            return RomanNumber._null()
        return RomanNumber(result)

    @staticmethod
    def _null():
        obj = RomanNumber.__new__(RomanNumber)
        obj.rom_value = obj.int_value = None
        return obj

    def _ioperation(self, other, op):
        result = self._operation(other, op)
        self.int_value, self.rom_value = result.int_value, result.rom_value
        return self

    __add__ = lambda s, o: s._operation(o, lambda a, b: a + b)
    __sub__ = lambda s, o: s._operation(o, lambda a, b: a - b)
    __mul__ = lambda s, o: s._operation(o, lambda a, b: a * b)
    __truediv__ = lambda s, o: s._operation(o, lambda a, b: a // b)
    __floordiv__ = __truediv__
    __mod__ = lambda s, o: s._operation(o, lambda a, b: a % b)
    __pow__ = lambda s, o: s._operation(o, lambda a, b: a ** b)

    __iadd__ = lambda s, o: s._ioperation(o, lambda a, b: a + b)
    __isub__ = lambda s, o: s._ioperation(o, lambda a, b: a - b)
    __imul__ = lambda s, o: s._ioperation(o, lambda a, b: a * b)
    __itruediv__ = lambda s, o: s._ioperation(o, lambda a, b: a // b)
    __ifloordiv__ = __itruediv__
    __imod__ = lambda s, o: s._ioperation(o, lambda a, b: a % b)

    @staticmethod
    def is_roman(value):
        if not isinstance(value, str) or not value:
            return False
        if any(c not in 'IVXLCDM' for c in value):
            return False
        invalid = ['IIII', 'XXXX', 'CCCC', 'MMMM', 'VV', 'LL', 'DD',
                   'IL', 'IC', 'ID', 'IM', 'XD', 'XM', 'VX', 'VL', 'VC', 'VD', 'VM',
                   'LC', 'LD', 'LM', 'DM']
        if any(p in value for p in invalid):
            return False
        prev, max_val = 0, 0
        for c in reversed(value):
            curr = RomanNumber._values[c]
            if curr < prev and curr * 10 < max_val:
                return False
            max_val = max(max_val, curr)
            prev = curr
        decimal = sum(RomanNumber._values[c] * (1 if RomanNumber._values[c] >= 
                      RomanNumber._values.get(n, 0) else -1) 
                      for c, n in zip(value, value[1:] + 'I'))
        return 0 < decimal < 4000

    @staticmethod
    def is_int(value):
        return isinstance(value, int) and 0 < value < 4000
