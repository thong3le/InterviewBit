class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        M = {0:'0', 1:'1', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        if len(A) == 0:
            return []
        if len(A) == 1:
            return list(M[int(A[0])])
        ans = []
        head = list(M[int(A[0])])
        tail = self.letterCombinations(A[1:])
        for h in head:
            for t in tail:
                ans.append(h+t)
        return ans
            