class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        j = 0
        n = len(A)
        for i in range(n):
            if A[i] <= 0:
                A[i],A[j] = A[j],A[i]
                j+=1
        for i in range(j,n):
            if abs(A[i])-1+j < n and A[abs(A[i])-1+j] > 0:
                A[abs(A[i])-1+j] = -A[abs(A[i])-1+j]
        
        for i in range(j,n):
            if A[i] > 0:
                return i-j+1
        return n - j + 1    
    
    def firstMissingPositive_2(self, A):
        b = set(A)
        for i in range(1,len(A)+2):
            if i not in b:
                return i