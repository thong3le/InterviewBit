class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        if len(A) < 4:
            return []
        d = {}
        result = None
        for i in range(len(A) - 1):
            for j in range(i+1, len(A)):
                if A[i] + A[j] in d:
                    k, l = d[A[i] + A[j]]
                    if len(set([i,j,k,l])) == 4:
                        if not result or result > [k,l,i,j]:
                            result = [k, l, i, j]
                else:
                    d[A[i]+A[j]] = (i,j)
        return result