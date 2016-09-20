class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        d = {}
        for e in A:
            if e in d:
                d[e] += 1
            else:
                d[e] = 1
        for e in d.keys():
            if d[e] > 1:
                return e