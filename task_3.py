import random


class NavalBattle:
    playing_field = None

    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def show():
        for row in NavalBattle.playing_field:
            print(''.join('~' if c in (0, 1) else str(c) for c in row))

    def shot(self, x, y):
        if NavalBattle.playing_field is None:
            print('игровое поле не заполнено')
            return
        cell = NavalBattle.playing_field[y - 1][x - 1]
        if cell in ('o', self.symbol):
            print('ошибка')
            return
        hit = cell == 1
        NavalBattle.playing_field[y - 1][x - 1] = self.symbol if hit else 'o'
        print('попал' if hit else 'мимо')

    @classmethod
    def new_game(cls):
        cls.playing_field = [[0] * 10 for _ in range(10)]
        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        
        def neighbors(x, y, size, horiz):
            cells = {(x + (i if horiz else 0) + dx, y + (0 if horiz else i) + dy)
                     for i in range(size) for dx in (-1, 0, 1) for dy in (-1, 0, 1)}
            return cells

        def can_place(x, y, size, horiz):
            if horiz and x + size > 10 or not horiz and y + size > 10:
                return False
            return all(0 <= nx < 10 and 0 <= ny < 10 and cls.playing_field[ny][nx] == 0
                      for nx, ny in neighbors(x, y, size, horiz))

        for size in ships:
            placed = False
            while not placed:
                x, y = random.randint(0, 9), random.randint(0, 9)
                horiz = random.choice([True, False])
                if can_place(x, y, size, horiz):
                    for i in range(size):
                        nx, ny = (x + (i if horiz else 0), y + (0 if horiz else i))
                        cls.playing_field[ny][nx] = 1
                    placed = True
