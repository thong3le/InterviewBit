from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        d = Counter(A)
        for e in d.keys():
            if d[e] > float(len(A))/3:
                return e
        return -1
