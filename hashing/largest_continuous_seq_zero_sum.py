class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        n = len(A)
        cum = [0]
        for i in range(n):
            cum.append(cum[-1] + A[i])
        d = {}
        left, right = 0, 0
        for i in range(n+1):
            if cum[i] in d:
                if i - d[cum[i]] > right - left:
                    left, right = d[cum[i]], i
            else:
                d[cum[i]] = i
        return A[left:right]
        