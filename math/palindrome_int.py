class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        s = str(A)
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True