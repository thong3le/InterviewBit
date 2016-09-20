class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        A.append(0)
        stack = [0]
        ans = 0
        for i in range(1, len(A)):
            while stack and A[i] < A[stack[-1]]:
                h = A[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, w * h)
            stack.append(i)
        return ans