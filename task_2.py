class NavalBattle:
    playing_field = None

    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def show():
        for row in NavalBattle.playing_field:
            print(''.join('~' if c in (0, 1) else str(c) for c in row))

    def shot(self, x, y):
        cell = NavalBattle.playing_field[y - 1][x - 1]
        hit = cell == 1
        NavalBattle.playing_field[y - 1][x - 1] = self.symbol if hit else 'o'
        print('попал' if hit else 'мимо')
