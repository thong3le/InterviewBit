class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        n = len(A)
        if n == 1:
            return [[A]]
        ans = []
        for i in range(1, n):
            if self.ispalindrome(A[:i]):
                tmp = self.partition(A[i:])
                for p in tmp:
                    ans.append([A[:i]] + p)
        if self.ispalindrome(A):
            ans.append([A])
        return ans
        
    def ispalindrome(self, s):
        return s == s[::-1]
