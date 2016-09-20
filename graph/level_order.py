# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        ans = []
        queue = deque([A])
        while queue:
            m = len(queue)
            level = []
            for _ in range(m):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                ans.append(level)
        return ans
                