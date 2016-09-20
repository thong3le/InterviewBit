# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        if A is None:
            return 0
        ans = 0
        stack = [(A, 0)]
        while stack:
            d, s = stack.pop()
            s = (10*s+d.val)%1003
            if d.left:
                stack.append((d.left, s))
            if d.right:
                stack.append((d.right, s))
            if d.left is None and d.right is None:
                ans = (ans + s)%1003
        return ans
        
    def sumNumbers1(self, A, s = 0):
        if A is None:
            return s
        s = (s*10 + A.val) % 1003
        if A.left is None and A.right is None:
            return s
        ans = 0
        if A.left:
            ans += self.sumNumbers1(A.left, s)
        if A.right:
            ans += self.sumNumbers1(A.right, s)
        return ans % 1003
