# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.cur = root
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack or self.cur

    # @return an integer, the next smallest number
    def next(self):
        while self.hasNext():
            if self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            else:
                node = self.stack.pop()
                self.cur = node.right
                return node.val
        return None
        