class Solution:
    # @param n : integer
    # @param k : integer
    # @return a strings
    
    def getPermutation(self, n, k):
        result = []
        fac = [1]
        for i in range(1, n):
            fac.append(i*fac[-1])
        A = [str(i) for i in range(1, n+1)]
        k -= 1
        while A:
            d, r = divmod(k, fac[len(A) - 1])
            result.append(A[d])
            A.pop(d)
            k = r
        return ''.join(result)