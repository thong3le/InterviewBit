class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        if len(A) == 0:
            return 0
        m, n = len(A), len(A[0])
        visited = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] != 'X' or (i,j) in visited:
                    continue
                count += 1
                stack = [(i,j)]
                visited.add((i,j))
                while stack:
                    a, b = stack[-1]
                    if a-1 >= 0 and A[a-1][b] == 'X' and (a-1,b) not in visited:
                        stack.append((a-1, b))
                        visited.add((a-1,b))
                    elif a+1 < m and A[a+1][b] == 'X' and (a+1, b) not in visited:
                        stack.append((a+1, b))
                        visited.add((a+1,b))
                    elif b-1 >= 0 and A[a][b-1] == 'X' and (a, b-1) not in visited:
                        stack.append((a, b-1))
                        visited.add((a, b-1))
                    elif b+1 < n and A[a][b+1] == 'X' and (a, b+1) not in visited:
                        stack.append((a, b+1))
                        visited.add((a,b+1))
                    else:
                        stack.pop()
        return count