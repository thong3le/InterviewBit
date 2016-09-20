class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        longest = 1
        ans = 0
        for i in range(1, n-1):
            p = 1
            l, r = i-1, i+1
            while l >= 0 and r <= n-1 and A[l] == A[r]:
                l -= 1
                r += 1
                p += 2
            if p > longest:
                longest = p
                ans = l+1
                
        for i in range(0, n-1):
            p = 0
            l, r = i, i+1
            while l >= 0 and r <= n-1 and A[l] == A[r]:
                l -= 1
                r += 1
                p += 2
            if p > longest:
                longest = p
                ans = l+1
                
        return A[ans:ans+longest]