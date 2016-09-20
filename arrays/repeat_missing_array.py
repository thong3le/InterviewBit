class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        sub = sum(A) - (n*(n+1))//2
        ss1 = ss2 = 0
        for i,e in enumerate(A):
            ss1 += e*e
            ss2 += (i+1) * (i+1)
        add = (ss1 - ss2)//sub
        
        return [(add+sub)//2, (add-sub)//2]