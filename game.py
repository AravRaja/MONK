class _24:
    def __init__(self):
        self.solution = '6*4'
        self.numbers = [6, 4, 1, 1]

    def equal(self, *numbers):  #24 Game Generator
        from operator import add, sub, mul
        from itertools import permutations
        from itertools import product
        div = lambda x, y: 9999999 if y == 0 else x / y
        for a, b, c, d in permutations(numbers):
            for x, y, z in product([(add, '+'), (sub, '-'), (mul, '*'),
                                    (div, '/')],
                                   repeat=3):
                if 24 == x[0](y[0](a, b), z[0](c, d)):
                    return f'({a}{y[1]}{b}){x[1]}({c}{z[1]}{d})'
                if 24 == x[0](y[0](z[0](a, b), c), d):
                    return f'(({a}{z[1]}{b}){y[1]}{c}){x[1]}{d}'
                if 24 == x[0](y[0](a, z[0](b, c)), d):
                    return f'({a}{y[1]}({b}{z[1]}{c})){x[1]}{d}'
                if 24 == x[0](a, y[0](b, z[0](c, d))):
                    return f'{a}{x[1]}({b}{y[1]}({c}{z[1]}{d}))'

        return False

    def generate(self):  #generates four numbers and solution
        from random import randint as r
        while True:
            a = r(1, 13)
            b = r(1, 13)
            c = r(1, 13)
            d = r(1, 13)
            solution = self.equal(a, b, c, d)
            if solution:
                self.solution = solution
                self.numbers = [a, b, c, d]
                return 'Finished Generation'

    def check(self, string):  #checks if user solution is valid
        target = self.numbers
        final = ''.join(['*' if i == 'x' else i for i in string])
        allowed = list('1234567890()*+-/')
        target = [str(i) for i in target]
        fake_target = list(''.join(target))

        for i in final:
            if i not in allowed:
                return 'no'
        try:
            if eval(final) == 24:
                number_checker = ''.join(
                    [i if i in fake_target else ' ' for i in final])

                number_checker = number_checker.split(' ')
                number_checker = [i for i in number_checker if i != '']
                if sorted(number_checker) == sorted(target):
                    return False
                else:
                    return 'Make sure to use all the numbers'
            return f'This equals {eval(final)} :('
        except:
            return 'Make sure your brackets line up'