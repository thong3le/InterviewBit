class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        count, max_len = 0, 0
        i, j, left, right = 0, 0, 0, 0
        while i < len(A):
            if A[i] == 0:
                count += 1
            if count > B:
                if i - j > max_len:
                    max_len = i - j
                    left, right = j, i
                while j <= i and count > B:
                    if A[j] == 0:
                        count -= 1
                    j += 1
            i += 1
        if i - j > max_len:
            left, right = j, i
        return list(range(left, right))