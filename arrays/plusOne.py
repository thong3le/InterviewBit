class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A.reverse()
        carry, A[0] = divmod(A[0] + 1, 10)
        for i in range(1, len(A)):
            carry, A[i] = divmod(carry + A[i], 10)
            if carry == 0:
                break
        else:
            A.append(carry)
        
        while A[-1] == 0:
            A.pop()
        A.reverse()
        return A