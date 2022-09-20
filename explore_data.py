import tree

characterData = ['a','b','c','d','e','f']

characterTree = tree.Tree()

for c in characterData:
    n = tree.Node(c)
    characterTree.insert(n)

characterTree.preorder(characterTree.head)
print(characterTree.treeSum(characterTree.head))

numberData = [0,1,2,3,4,5]

numberTree = tree.Tree()

for i in numberData:
    n = tree.Node(i)
    numberTree.insert(n)

numberTree.breadth(True)
print(numberTree.treeSum(numberTree.head))