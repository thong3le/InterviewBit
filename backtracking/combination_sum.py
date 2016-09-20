class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = list(set(A))
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
        cur.append(A[i])
        self.recurse(result, cur, A, B - A[i], i)
        cur.pop()
        self.recurse(result, cur, A, B, i+1)