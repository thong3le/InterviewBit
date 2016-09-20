class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        chars = []
        for c in A:
            if c.isalnum():
                chars.append(c.lower())
        n = len(chars)
        for i in range(n//2):
            if chars[i] != chars[n-1-i]:
                return 0
        return 1