class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        l = 0
        r = len(A) - 1
        ans = 0
        while l < r:
            ans = max(ans, (r-l)*min(A[l], A[r]))
            if A[l] < A[r]:
                l += 1
            else: 
                r -= 1
        return ans