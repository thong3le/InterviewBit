# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        result = []
        stack = []
        cur = A
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                result.append(stack[-1].val)
                cur = stack.pop().right
        return result