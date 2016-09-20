# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    def depth(self, A):
        if A is None:
            return (-1, True) 
        l, b1 = self.depth(A.left)
        r, b2 = self.depth(A.right)
        return (1 + max(l, r), b1 and b2 and abs(l-r) <= 1)
        
    def isBalanced(self, A):
        return self.depth(A)[1]