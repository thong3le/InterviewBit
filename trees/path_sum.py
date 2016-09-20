# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if A is None:
            return False
        if A.left is None and A.right is None:
            return A.val == B
        return self.hasPathSum(A.left, B - A.val) or self.hasPathSum(A.right, B - A.val) 


