class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        max_ending_here = min_ending_here = max_so_far = A[0]
        for i in range(1, len(A)):
            if A[i] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here
            max_ending_here = max(A[i], max_ending_here * A[i])
            min_ending_here = min(A[i], min_ending_here * A[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far