'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], exact = False) -> bool:

        if not root and not subRoot:
            return True

        if not root and subRoot:
            return False

        if root and not subRoot:
            return False

        if not exact:

            if root.val == subRoot.val:

                leftSide = self.isSubtree(root.left,subRoot.left, True)
                rightSide = self.isSubtree(root.right,subRoot.right, True)

                if leftSide and rightSide:
                    return True

            leftSide = self.isSubtree(root.left,subRoot)
            if leftSide:
                return True

            return self.isSubtree(root.right,subRoot)

        if root.val != subRoot.val:
            return False

        leftSide = self.isSubtree(root.left,subRoot.left, True)
        rightSide = self.isSubtree(root.right,subRoot.right, True)  

        return leftSide and rightSide

            
