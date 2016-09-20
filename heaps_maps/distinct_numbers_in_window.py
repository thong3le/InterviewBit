from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        result = []
        if B > len(A):
            return result
        counts = Counter(A[:B])
        result.append(len(counts))
        for i in range(B, len(A)):
            d = A[i-B]
            counts[d] -= 1
            if counts[d] == 0:
                counts.pop(d)
            counts[A[i]] = counts.get(A[i], 0) + 1
            result.append(len(counts))
        return result
            