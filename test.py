from reliability import Node

nodes = Node.list(0.99, 0.98, 0.98)

for node in nodes:
    print(node)
print()

print(
    nodes[0] & (nodes[1] | nodes[2])
)

print('\n################\n')

a1 = Node(0.99, 'Сервер 1')
print(a1)

a2 = Node(0.6, 'Сервер 2')

print(a1 & a2)
print(a1 | a2)
