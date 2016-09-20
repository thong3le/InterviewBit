class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        pascal = [[1],[1,1]]
        for i in range(2, A+1):
            row = [1] * (i+1)
            for k in range(1, i):
                row[k] = pascal[-1][k-1] + pascal[-1][k]
            pascal.append(row)
        return pascal[:A]