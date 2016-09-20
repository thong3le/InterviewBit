class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        n = len(A)
        if n == 0:
            return []
        cum = [A[0]]
        for i in range(1, n):
            cum.append(cum[-1] + A[i])
        d = {}
        left, right = 0, 0
        for i in range(n):
            if cum[i] in d and i - d[cum[i]] + 1 > right - left:
                left, right = d[cum[i]], i+1
            else:
                d[cum[i]] = i
        print(cum)
        print(d)
        return A[left:right]


A = [1,2,-3,3]
S = Solution()

print(S.lszero(A))