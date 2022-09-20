import tree

data = ['a','b','c','d','e','f']

t = tree.Tree()

for c in data:
    n = tree.Node(c)
    t.insert(n)

t.breadth()
