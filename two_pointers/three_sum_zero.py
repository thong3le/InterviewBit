class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        ans = set()
        A.sort()
        n = len(A)
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                temp = A[i] + A[j] + A[k]
                if temp == 0:
                    ans.add((A[i], A[j], A[k]))
                if temp <= 0:
                    j += 1
                else:
                    k -= 1
        return list(ans)