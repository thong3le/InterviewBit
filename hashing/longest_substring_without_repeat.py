class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        d = {}
        cur, result = 0, 0
        for j in range(len(A)):
            if A[j] in d and d[A[j]] >= cur:
                cur = d[A[j]] + 1
            else:
                result = max(result, j - cur + 1)
            d[A[j]] = j
        return result