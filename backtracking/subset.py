class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self,A):
        A.sort()
        result = []
        self.generate(result, [], A, 0)
        result.sort()
        return result
        
    def generate(self, result, cur, A, i):
        if i == len(A):
            result.append(list(cur))
        else:
            
            self.generate(result, cur, A, i+1)
            
            cur.append(A[i])
            self.generate(result, cur, A, i+1)
            cur.pop()