# Copyright © 2020 Aleksandr Kolbasov

from reliability import Node

nodes = Node.list(0.99, 0.8, 0.8, 0.8)

for node in nodes:
    print(node)

print(
    """
             /---node_1---\\
            |              |
---node_0---+----node_2----+---
            |              |
             \\---node_3---/
    """
)

print(
    nodes[0] & (nodes[1] | nodes[2] | nodes[3])
)
print(
    nodes[0] * (nodes[1] + nodes[2] + nodes[3])
)
print(
    Node.serial(0.99, Node.parallel(0.8, 0.8, 0.8))
)

print('\n################\n')

a1 = Node(0.99, 'Сервер 1')
a2 = Node(0.6)
print("{}\nСервер 2: {}\n".format(a1, a2))

print("Последовательно: ", a1 & a2)
print("Параллельно: ", a1 | a2)

print("Последовательно: {}".format(
    Node.serial(0.99, 0.6)
))
print("Параллельно: {}".format(
    Node.parallel(a1.p, a2.p)
))
