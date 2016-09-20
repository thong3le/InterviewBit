class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for c in A:
            if c != ')':
                stack.append(c)
            else:
                expr = []
                while stack[-1] != '(':
                    expr.append(stack.pop())
                stack.pop()
                if len(expr) <= 1:
                    return 1
        return 0