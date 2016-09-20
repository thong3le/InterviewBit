class Solution:
    # @param A : integer
    # @return a list of strings
    
    def generateParenthesis(self, A):
        result = []
        self.recursion(result, [], A, 0, 0)
        return result
        
    def recursion(self, result, cur, A, s, e):
        if s == A and e == A:
            result.append(''.join(cur))
            return
        if s > A or e > A:
            return
        
        if s < A:
            cur.append('(')
            self.recursion(result, cur, A, s+1, e)
            cur.pop()
        
        if s > e:
            cur.append(')')
            self.recursion(result, cur, A, s, e+1)
            cur.pop()