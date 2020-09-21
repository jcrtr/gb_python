from random import randint


def generate_unique_numbers(count, minbound, maxbound):
    if count > maxbound - minbound + 1:
        raise ValueError('Некорретные параметры')
    ret = []
    while len(ret) < count:
        new = randint(minbound, maxbound)
        if new not in ret:
            ret.append(new)
    return ret


class Keg:
    numbers = None

    def __init__(self):
        self.numbers = randint(1, 90)

    @property
    def num(self):
        return self.numbers

    def __str__(self):
        return str(self.numbers)


class Card:
    rows = 3
    cols = 9
    nums_row = 5
    data = None
    empty_num = 0
    crossed_num = -1

    def __init__(self):
        _uniques = self.nums_row * self.rows
        uniques = generate_unique_numbers(_uniques, 1, 90)
        self.data = []
        for i in range(0, self.rows):
            tmp = sorted(uniques[self.nums_row * i: self.nums_row * (i + 1)])
            empty_nums_count = self.cols - self.nums_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self.empty_num)
            self.data += tmp

    def __str__(self):
        line = '--------------------------'
        ret = line + '\n'
        for index, num in enumerate(self.data):
            if num == self.empty_num:
                ret += '  '
            elif num == self.x_num:
                ret += ' x'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.cols == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + line

    def __contains__(self, item):
        return item in self.data

    def x_num(self, num):
        for index, item in enumerate(self.data):
            if item == num:
                self.data[index] = self.x_num
                return
        raise ValueError(f'Нет номера: {num}')

    def closed(self) -> bool:
        return set(self.data) == {self.empty_num, self.crossed_num}


class Game:
    user = None
    comp = None
    num_kegs = 90
    kegs = []
    gameover = False

    def __init__(self):
        self.user = Card()
        self.comp = Card()
        self.kegs = generate_unique_numbers(self.num_kegs, 1, 90)

    @property
    def play_round(self) -> int:
        keg = self.kegs.pop()
        print(f'Новый бочонок {keg}, (осталось {len(self.kegs)})')
        print(f'Игрок:\n{self.user}')
        print(f'Карточка компьютера: \n{self.comp}')
        user_answer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if user_answer == 'y' and not keg in self.user or user_answer != 'y' and keg in self.user:
            return 2

        if keg in self.user:
            self.user.x_num(keg)
            if self.user.closed():
                return 1
        if keg in self.comp:
            self.comp.x_num(keg)
            if self.comp.closed():
                return 2
        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round
        if score == 1:
            print('Вы выиграли')
            break
        elif score == 2:
            print('Вы проиграли')
            break