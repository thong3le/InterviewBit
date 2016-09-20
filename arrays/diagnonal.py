class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
    def diagonal(self, a):
        n = len(a)
        res = []
        for i in range(n):
            row = [0] * (i+1)
            for j in range(i+1):
                row[j] = a[j][i-j]
            res.append(row)
        for i in range(1, n):
            row = [0] * (n-i)
            for j in range(n-i):
                row[j] = a[i+j][n-1-j]
            res.append(row)
        return res

a = Solution()
print(a.diagonal([[1,2,3],[4,5,6],[7,8,9]]))
