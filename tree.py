class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head == None:
            self.head = node
            return
        
        queue = []
        queue.append(self.head)
    
        while len(queue):
            temp = queue[0]
            queue.pop(0)
    
            if (not temp.left):
                temp.left = node
                break
            else:
                queue.append(temp.left)
    
            if (not temp.right):
                temp.right = node
                break
            else:
                queue.append(temp.right)

    def postorder(self, node):
        if node.left != None:
            self.postorder(node.left)
        
        if node.right != None:
            self.postorder(node.right)

        print(node.data)

    def preorder(self, node):
        print(node.data)

        if node.left != None:
            self.postorder(node.left)
        
        if node.right != None:
            self.postorder(node.right)

    def breadth(self):
        if self.head == None:
            return

        queue = [self.head]

        while len(queue):
            front = queue.pop(0)

            if front.left != None:
                queue.append(front.left)
            if front.right != None:
                queue.append(front.right)

            print(front.data)

    def includes(self, needle):
        if self.head == None:
            return False
        
        if self.head.data == needle:
            return True

        queue = [self.head]

        while len(queue) > 0:
            front = queue.pop(0)
            if front.data == needle:
                return True
            
            if front.left != None:
                queue.append(front.left)
            if front.right != None:
                queue.append(front.right)
        
        return False