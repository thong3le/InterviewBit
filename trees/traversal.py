class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        result = []
        stack = []
        cur = A
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                result.append(stack[-1].val)
                cur = stack.pop().right
        return result

    def postorderTraversal(self, A):
        result = []
        stack = [A]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

    def preorderTraversal(self, A):
        result = []
        stack = [A]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result