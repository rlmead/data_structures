import numbers

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
            self.preorder(node.left)
        
        if node.right != None:
            self.preorder(node.right)

    def breadth(self, withRelationships = False):
        if self.head == None:
            return

        queue = [self.head]

        while len(queue):
            front = queue.pop(0)

            if front.left != None:
                queue.append(front.left)
            if front.right != None:
                queue.append(front.right)

            if withRelationships:
                front_left_data = front.left.data if front.left else 'None'
                front_right_data = front.right.data if front.right else 'None'
                print(str(front.data) + ': left child = ' + str(front_left_data) + ', right child = ' + str(front_right_data))
            else:
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

    def treeSum(self, node):
        if node.left == None and node.right == None:
            return node.data

        if not isinstance(node.data, numbers.Number):
            print('whoops, the treeSum() function only works on trees that hold number data!')
            return

        total = node.data

        node_left_data = self.treeSum(node.left) if node.left else 0
        node_right_data = self.treeSum(node.right) if node.right else 0

        return total + node_left_data + node_right_data

    def treeMin(self, node):
        if node == None:
            return float('inf')

        if not isinstance(node.data, numbers.Number):
            print('whoops, the treeMin() function only works on trees that hold number data!')
            return
        
        leftMin = self.treeMin(node.left)
        rightMin = self.treeMin(node.right)

        return min(leftMin, rightMin, node.data)

    def treeMax(self, node):
        if node == None:
            return -float('inf')

        if not isinstance(node.data, numbers.Number):
            print('whoops, the treeMax() function only works on trees that hold number data!')
            return

        leftMax = self.treeMax(node.left)
        rightMax = self.treeMax(node.right)

        return max(leftMax, rightMax, node.data)
