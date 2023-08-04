# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            # Traverse down the left subtree and store nodes in the stack
            while current:
                stack.append(current)
                current = current.left

            # Pop the node from the stack and visit it
            current = stack.pop()
            result.append(current.val)

            # Traverse the right subtree
            current = current.right

        return result

# Test the inorderTraversal function
if __name__ == "__main__":
    # Create a sample binary tree: 1
    #                             /  \
    #                           null  2
    #                                /
    #                               3
    root = TreeNode(1)
    root.left = TreeNode('null')
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    inorder_result = solution.inorderTraversal(root)
    print(inorder_result)  # Output: [1, null, 2 ,3]
