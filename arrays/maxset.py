class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        for e in A:
            if e >= 0:
                break
        else:
            return []
        
        start = 0
        L, R = 0, 0
        lmax, gmax = 0, 0
        
        for i, e in enumerate(A):
            if e >= 0:
                lmax += e
            else:
                start = i+1
                lmax = 0
            
            if lmax > gmax:
                L, R = start, i
                gmax = lmax
            if lmax == gmax and R - L < i - start:
                L, R = start, i
        
        return A[L:R+1]