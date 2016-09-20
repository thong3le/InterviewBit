class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        return len(A.split()[-1]) if A.split() else 0
