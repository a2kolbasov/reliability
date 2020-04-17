# Copyright (c) 2020 Alexander Kolbasov

from reliability import Node

nodes = Node.list(0.99, 0.98, 0.98)

for node in nodes:
    print(node)
print()

print(
    nodes[0] & (nodes[1] | nodes[2])
    #nodes[0] * (nodes[1] + nodes[2])

    ##               /---node_1---\
    ##  ---node_0---|              |---
    ##               \---node_2---/
)

print('\n################\n')

a1 = Node(0.99, 'Сервер 1')
a2 = Node(0.6)
print("{}\nСервер 2: {}\n".format(a1, a2))

print("Последовательно: ", a1 & a2)
print("Параллельно: ", a1 | a2)
