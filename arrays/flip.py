class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        d = {'0':1, '1':-1}
        a = [d[c] for c in A if c != '\n']
        ones = a.count(-1)
        if ones == len(a):
            return []
        
        lmax = gmax = 0
        start = 0
        L = R = 0
        
        for i,e in enumerate(a):
            lmax += e
            if lmax < 0:
                start = i+1
                lmax = 0
            if gmax < lmax:
                L = start
                R = i
                gmax = lmax
        return [L+1,R+1]