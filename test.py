from reliability import Node

a1 = Node(0.9, 'a1')
a2 = Node(0.7)

print(a1)
print(a2)
print(a1 & a2 & (a1 | a2 | a2))

print()

lst = Node.list(1, 0.5, 0.3, 0.4)
for i in lst:
    print(lst)
print(lst)
