class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack = []
        for c in A:
            if c in set(['(', '{', '[']):
                stack.append(c)
            else:
                if not stack or (stack.pop() + c) not in set(['()', '{}','[]']):
                    return 0
        return 0 if stack else 1