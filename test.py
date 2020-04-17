from reliability import Node

a1 = Node(0.9, 'a1')
a2 = Node(0.7)

print(a1)
print(a2)
print(a1 & a2 & (a1 | a2 | a2))
