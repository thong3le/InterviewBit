from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        d = Counter(A)
        for k, v in d.items():
            if v > len(A)//2:
                return k
        return -1