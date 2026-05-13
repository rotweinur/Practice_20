class RomanNumber:
    _values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, value):
        self.rom_value = value if self.is_roman(value) else None
        if not self.rom_value:
            print('ошибка')

    def decimal_number(self):
        if not self.rom_value:
            return None
        result = 0
        for curr, next_char in zip(self.rom_value, self.rom_value[1:] + 'I'):
            result += self._values[curr] * (1 if self._values[curr] >= self._values[next_char] else -1)
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
