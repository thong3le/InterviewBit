# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if len(A) == 0:
            return None
        i = A.index(max(A))
        root = TreeNode(A[i])
        root.left = self.buildTree(A[:i])
        root.right = self.buildTree(A[i+1:])
        return root 