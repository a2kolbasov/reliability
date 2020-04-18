# Copyright © 2020 Aleksandr Kolbasov

"""
Позволяет вычислять вероятность безотказной работы соединённых узлов
"""


class Node:
    """Узел в цепи"""

    @classmethod
    def list(cls, *probabilities: float) -> list:
        """
        Возвращает list из Nodes с заданными вероятностями
        """
        return list(cls(
            node[1], str(node[0])
        ) for node in enumerate(probabilities))

    @classmethod
    def parallel(cls, *probabilities: float):
        """
        Соединить узлы параллельно в единый блок
        :param probabilities: Вероятность безотказной работы присоединяемого узла
        :return: Единый блок
        """
        nodes = cls.list(*probabilities)
        final_node = cls(0)
        for node in nodes:
            final_node |= node
        return final_node

    @classmethod
    def serial(cls, *probabilities: float):
        """
        Соединить узлы последовательно в единый блок
        :param probabilities: Вероятность безотказной работы присоединяемого узла
        :return: Единый блок
        """
        nodes = cls.list(*probabilities)
        final_node = cls(1)
        for node in nodes:
            final_node &= node
        return final_node

    @property
    def p(self) -> float:
        """Вероятность безотказной работы"""
        return self._p

    @p.setter
    def p(self, probability: float):
        """Вероятность безотказной работы"""
        assert 0 <= probability <= 1
        self._p = probability

    @property
    def q(self):
        """Вероятность отказа"""
        return 1 - self.p

    @q.setter
    def q(self, probability):
        """Вероятность отказа"""
        self.p = 1 - probability

    def __init__(self, p: float, name: str = ''):
        """
        Узел в цепи
        :param p: Вероятность безотказной работы
        :param name: Имя узла
        """

        if p is None:
            raise Exception("Не задана вероятность")

        p = float(p)
        if 0 <= p <= 1:
            self.p = p
            self.name = str(name)
        else:
            raise Exception("Неверная вероятность")

    def __add__(self, other):
        """Параллельное соединение"""
        return self | other

    def __mul__(self, other):
        """Последовательное соединение"""
        return self & other

    def __or__(self, other):
        """Параллельное соединение"""
        q = self.q * other.q
        return self.__class__(1 - q)

    def __and__(self, other):
        """Последовательное соединение"""
        p = self.p * other.p
        return self.__class__(p)

    def __str__(self):
        return "P{name} = {p}".format(p=self.p, name="({})".format(self.name) if self.name != '' else '')

    def __float__(self):
        """Вероятность безотказной работы узла"""
        return self.p
