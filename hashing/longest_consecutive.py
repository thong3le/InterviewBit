class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A = sorted(set(A))
        m = 1
        c = 1
        for i in range(1, len(A)):
            if A[i] - 1 == A[i-1]:
                c += 1
            else:
                print(m , c)
                m = max(c, m)
                c = 1
        return max(m,c)

A = [6,4,5,3,2]
print(Solution().longestConsecutive(A))