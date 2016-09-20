class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        for s in A:
            if s in ['+','-','*','/']:
                a = stack.pop()
                b = stack.pop()
                stack.append(str(eval(b+s+a)))
            else:
                stack.append(s)
        return int(stack[-1])