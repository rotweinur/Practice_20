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
        num = self.int_value
        return ''.join(sym * (num // val) for val, sym in self._numerals if (num %= val, True)[1])

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
