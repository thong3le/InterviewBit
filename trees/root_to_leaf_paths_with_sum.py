# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, sum1):
        self.result = []
        if root is None:
            return self.result
        self.paths(root, sum1, [])
        return self.result
        
    def paths(self, root, sum1, p):
        if root.left is None and root.right is None and root.val == sum1:
            self.result.append(p + [root.val])
            return
        if root.left:
            self.paths(root.left, sum1 - root.val, p + [root.val])
        if root.right:
            self.paths(root.right, sum1 - root.val, p + [root.val])
