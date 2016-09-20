class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        stack = []
        total = 0
        for i in range(len(A)):
            while stack and A[i] >= A[stack[-1]]:
                j = stack.pop()
                if not stack:
                    break
                total += (i - stack[-1] - 1) * (min(A[stack[-1]], A[i]) - A[j])
            stack.append(i)
        return total