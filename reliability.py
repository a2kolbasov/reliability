# Copyright © 2020 Aleksandr Kolbasov


class Obj:

    @property
    def p(self) -> float:
        return self._p
        # return

    @p.setter
    def p(self, probability: float):
        self._p = probability if (0 <= probability <= 1) else 0 if probability < 0 else 1

    @property
    def q(self):
        return 1 - self.p

    @q.setter
    def q(self, probability):
        self.p = 1 - probability

    def __init__(self, p: float):
        # self._p = 0.0

        def valid(probability):
            return 0 <= probability <= 1

        if p is None:
            raise Exception("Не задана ни одна вероятность")

        if valid(p):
            self.p = p
        else:
            raise Exception("Неверная вероятность")

    def __add__(self, other):
        print('add')
        return self | other

    def __mul__(self, other):
        print('mul')
        return self & other

    def __or__(self, other):
        print('or')
        Q = self.q * other.q
        return Obj(1 - Q)

    def __and__(self, other):
        print('and')
        Q = self.q + other.q
        return Obj(1 - Q)

    def __str__(self):
        return "p = {}".format(self.p)


p1 = Obj(0.9)
p2 = Obj(0.7)

print( p1 & p1 & (p2 | p2 | p2) )
