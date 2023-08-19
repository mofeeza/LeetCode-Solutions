# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(left, right):
            # Base case: if both nodes are None, they are symmetric
            if not left and not right:
                return True
            # If one of the nodes is None while the other is not, they are not symmetric
            if not left or not right:
                return False
            # Check if the values are equal and their subtrees are mirrors
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        # Start the recursion from the root's left and right subtrees
        return isMirror(root.left, root.right)
