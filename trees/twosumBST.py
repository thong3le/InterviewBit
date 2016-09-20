class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        self.p1 = A
        self.p2 = A
        self.stack1 = []
        self.stack2 = []
        
        def next():
            while self.p1 or self.stack1:
                if self.p1:
                    self.stack1.append(self.p1)
                    self.p1 = self.p1.left
                else:
                    self.p1 = self.stack1.pop()
                    ans = self.p1.val
                    self.p1 = self.p1.right
                    return ans
            return None
        
        def prev():
            while self.p2 or self.stack2:
                if self.p2:
                    self.stack2.append(self.p2)
                    self.p2 = self.p2.right
                else:
                    self.p2 = self.stack2.pop()
                    ans = self.p2.val
                    self.p2 = self.p2.left
                    return ans
            return None
        
        i = next()
        j = prev()
        while i and j and i < j:
            if i + j == B:
                return 1
            elif i + j < B:
                i = next()
            else:
                j = prev()
        return 0