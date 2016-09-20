class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        result = []
        self.partion_helper(result, [], A, 0)
        return result
    
    def partion_helper(self, result, cur, A, i):
        if i == len(A):
            result.append(list(cur))
        for j in range(i, len(A)):
            if self.ispalindrome(A[i:j+1]):
                cur.append(A[i:j+1])
                self.partion_helper(result, cur, A, j+1)
                cur.pop()
        
    def ispalindrome(self, s):
        return s == s[::-1]