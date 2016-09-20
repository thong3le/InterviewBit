from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        A.sort()
        n = len(A)
        if n < 4:
            return []
        result = []
        for i in range(n-3):
            if i > 0 and A[i] == A[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and A[j] == A[j-1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    temp = A[i] + A[j] + A[k] + A[l]
                    if temp == B:
                        result.append((A[i],A[j], A[k],A[l]))
                        k += 1
                        while k < l and A[k] == A[k-1]:
                            k += 1
                    elif temp < B:
                        k += 1
                    else:
                        l -= 1
        return result
                    