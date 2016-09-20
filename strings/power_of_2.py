class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A = int(A)
        if A < 2:
            return 0
        while A > 2:
            A, r = divmod(A, 2)
            if r > 0: 
                return 0
        return 1