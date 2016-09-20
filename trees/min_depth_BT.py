# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if A is None:
            return 0
        if A.left is None and A.right is None:
            return 1
        if A.left is None:
            return 1 + self.minDepth(A.right)
        if A.right is None:
            return 1 + self.minDepth(A.left)
        return 1 + min(self.minDepth(A.right), self.minDepth(A.left))