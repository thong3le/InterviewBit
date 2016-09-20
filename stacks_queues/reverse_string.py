class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stack = []
        for c in A:
            stack.append(c)
        ans = []
        for _ in range(len(stack)):
            ans.append(stack.pop())
        return ''.join(ans)