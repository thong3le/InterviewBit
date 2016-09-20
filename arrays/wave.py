class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        print(A)
        for i in range(len(A)//2):
        	A[2*i],A[2*i+1] = A[2*i+1],A[2*i]
        return A

sol = Solution()
print(sol.wave([3,2,1,5,4]))