# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return True if A is None else self.isSymmetricHelper(A.left, A.right)
        
    def isSymmetricHelper(self, A, B):
        return A == B if A is None or B is None else A.val == B.val and self.isSymmetricHelper(A.left, B.right) and self.isSymmetricHelper(A.right, B.left)




