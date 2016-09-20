# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST1(self, A, lo = -float('inf'), hi = float('inf')):
        if A is None:
            return True
        if lo < A.val < hi and self.isValidBST(A.left, lo, A.val) and self.isValidBST(A.right, A.val, hi):
            return True
        else:
            return False
    def isValidBST(self, A):
        result = []
        self.inorder(result, A)
        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return 0
        return 1
        
    def inorder(self, result, A):
        if A is None:
            return
        self.inorder(result, A.left)
        result.append(A.val)
        self.inorder(result, A.right)
        