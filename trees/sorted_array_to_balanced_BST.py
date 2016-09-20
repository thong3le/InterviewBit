# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A, lo = None, hi = None):
        if lo is None and hi is None:
            lo, hi = 0, len(A)
        if lo == hi:
            return None
        mid = (lo + hi)//2
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A, lo, mid)
        root.right = self.sortedArrayToBST(A, mid+1, hi)
        return root