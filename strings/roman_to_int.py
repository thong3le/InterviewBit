class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i, c in enumerate(A):
            if i < len(A) - 1 and d[A[i]] < d[A[i+1]]:
                ans -= d[c]
            else:
                ans += d[c]
        return ans