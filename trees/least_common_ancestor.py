# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param val1 : integer
    # @param val2 : integer
    # @return an integer
    def search(self, result, A, x, path):
        if A is None:
            return 
        if A.val == x:
            result.extend(path + [A.val])
            return 
        self.search(result, A.left, x, path + [A.val])
        self.search(result, A.right, x, path + [A.val])
        
    def lca(self, A, val1, val2):
        p1 = []
        self.search(p1, A, val1, [])
        p2 = []
        self.search(p2, A, val2, [])
        if not p1 or not p2:
            return -1
        i = 0
        while i < len(p1) and i < len(p2) and p1[i] == p2[i]:
            i += 1
        return p1[i-1]