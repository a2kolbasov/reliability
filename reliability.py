# Copyright © 2020 Aleksandr Kolbasov


class Node:
    """Узел в цепи"""

    @property
    def p(self) -> float:
        """Вероятность безотказной работы"""
        return self._p

    @p.setter
    def p(self, probability: float):
        self._p = probability if (0 <= probability <= 1) else 0 if probability < 0 else 1

    @property
    def q(self):
        """Вероятность отказа"""
        return 1 - self.p

    @q.setter
    def q(self, probability):
        self.p = 1 - probability

    def __init__(self, p: float, name: str = ''):
        """
        Узел в цепи
        :param p: Вероятность безотказной работы
        :param name: Имя узла
        """

        if p is None:
            raise Exception("Не задана вероятность")

        if 0 <= p <= 1:
            self.p = p
            self.name = name
        else:
            raise Exception("Неверная вероятность")

    def __add__(self, other):
        return self | other

    def __mul__(self, other):
        return self & other

    def __or__(self, other):
        """Параллельное соединение"""
        q = self.q * other.q
        return Node(1 - q)

    def __and__(self, other):
        """Последовательное соединение"""
        q = self.q + other.q
        return Node(1 - q)

    def __str__(self):
        return "P{name} = {p}".format(p=self.p, name="({})".format(self.name) if self.name != '' else '')


p1 = Node(0.9, 'p1')
p2 = Node(0.7)

print(p1)
print(p2)
print( p1 & p1 & (p2 | p2 | p2) )
