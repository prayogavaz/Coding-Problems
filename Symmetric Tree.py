# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        if root.right == None and root.left == None:
            return True

        if root.right == None and root.left != None:
            return False

        if root.right != None and root.left == None:
            return False

        if root.right.val != root.left.val:
            return False

        leftTree = self.inOrderLeftFirst(root.left)
        rightTree = self.inOrderRightFirst(root.right)

        return all(x == y for x, y in zip(leftTree, rightTree))

    def inOrderLeftFirst(self, root: Optional[TreeNode]) -> list:

        if root.left == None and root.right == None:
            return [root.val]

        leftList = ['#']
        if root.left != None:
            leftList = self.inOrderLeftFirst(root.left)

        rightList = ['#']
        if root.right != None:
            rightList = self.inOrderLeftFirst(root.right)

        return leftList + [root.val] + rightList

    def inOrderRightFirst(self, root: Optional[TreeNode]) -> list:

        if root.left == None and root.right == None:
            return [root.val]

        rightList = ['#']
        if root.right != None:
            rightList = self.inOrderRightFirst(root.right)

        leftList = ['#']
        if root.left != None:
            leftList = self.inOrderRightFirst(root.left)

        return rightList + [root.val] + leftList
