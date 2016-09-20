class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        ans = 0
        for i in range(1, len(X)):
            ans += max(abs(X[i]-X[i-1]), abs(Y[i] - Y[i-1]))
        return ans