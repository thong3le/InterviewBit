class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        i, j, n, m = 0, 0, len(A), len(B)
        ans = []
        while i < n and j < m:
            if A[i] <= B[j]:
                ans.append(A[i])
                i += 1
            else:
                ans.append(B[j])
                j += 1
        ans.extend(A[i:n])
        ans.extend(B[j:m])
        return ans