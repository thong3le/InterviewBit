class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        cur_max = A[0]
        max_so_far = A[0]
        for e in A[1:]:
            cur_max = max(e, cur_max + e)
            max_so_far = max(cur_max, max_so_far)
        return max_so_far