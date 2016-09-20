class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        state = 0
        count = 0
        for b in A:
            if b == state:
                count += 1
                state = 1 - state
        return count