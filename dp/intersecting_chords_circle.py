class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        count = [0] * (A+1)
        count[0] = count[1] = 1
        for i in range(2, A+1):
            for j in range(i):
                count[i] = (count[i] + count[j]*count[i-1-j])% 1000000007
        return count[A]
