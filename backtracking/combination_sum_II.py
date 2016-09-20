class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        result = []
        self.recurse(result, [], A, B, 0)
        return result
        
    def recurse(self, result, cur, A, B, i):
        if B == 0:
            result.append(list(cur))
            return
        if i >= len(A) or B < 0:
            return
        j = i+1
        while j < len(A) and A[j] == A[i]: 
            j += 1
        for k in range(j-i+1):
            for _ in range(k):
                cur.append(A[i])
            self.recurse(result, cur, A, B-k*A[i], j)
            for _ in range(k):
                cur.pop()
