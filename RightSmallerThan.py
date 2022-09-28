'''Write a function that takes in an array of integers and returns an array of the same length, where each element in the output array corresponds to the number of integers in the input array that are to the right of the relevant index and that are strictly smaller than the integer at that index.

In other words, the value at output[i] represents the number of integers that are to the right of i and that are strictly smaller than input[i].'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):

        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def countStrictLessthanNodes(self,value):
            
            if value > self.value:
                result = 1
                if self.left != None:
                    result += self.left.countNodes()
                if self.right != None:
                    result += self.right.countStrictLessthanNodes(value)
                return result
            elif value == self.value:
                if self.left != None:
                    return self.left.countNodes()
                else:
                    return 0
            else: #value < self.value
                if self.left != None:
                    return self.left.countStrictLessthanNodes(value)
                else:
                    return 0

    def countNodes(self):

            nodes = 1
            
            if self.left != None:
                nodes += self.left.countNodes()
            if self.right != None:
                nodes += self.right.countNodes()

            return nodes


def rightSmallerThan(array):

    if len(array) == 0:
        return []

    result = [0 for i in range(len(array))]

    bst = BST(array[-1])

    for j in range(len(array)-2,-1,-1):
        bst.insert(array[j])
        result[j] = bst.countStrictLessthanNodes(array[j])

    return result
