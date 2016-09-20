class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A.sort()
        result = []
        self.subsetsWithDup_2(result, [], A, 0)
        return sorted(result)
    
    def subsetsWithDup_2(self, result, cur, A, i):
        if i == len(A):
            result.append(list(cur))
            return
        j = i + 1
        while j < len(A) and A[j] == A[i]:
            j += 1
        for k in range(j-i+1):
            for _ in range(k):
                cur.append(A[i])
            self.subsetsWithDup_2(result, cur, A, j)
            for _ in range(k):
                cur.pop()
