class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        
        if A == 1:
            return True
        if A == 2 or A == 3:
            return False
            
        for i in xrange(2, 33):
            B = int(round(pow(A, 1.0/i)))
            if B**i == A:
                return True
        return False