class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        n = len(A)
        m = len(A[0])
        LIMIT = min(n//2, m//2)
        for i in range(LIMIT):
            for j in range(i, m-1-i):
                result.append(A[i][j])
            for j in range(i, n-1-i):
                result.append(A[j][m-1-i])
            for j in range(m-1-i, i, -1):
                result.append(A[n-1-i][j])
            for j in range(n-1-i, i, -1):
                result.append(A[j][i])
        if min(m,n) % 2 != 0:
            if m >= n:
                i = n//2
                print(i)
                for j in range(i, m-1-i+1):
                    result.append(A[i][j])
            else:
                i = m//2
                for j in range(i, n-1-i+1):
                    result.append(A[j][i])
                
        return result

a = Solution()
print(a.spiralOrder([[1]]))