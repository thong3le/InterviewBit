class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fib = [1,1]
        while fib[-1] + fib[-2] <= A:
            fib.append(fib[-1] + fib[-2])
        ans = 0
        i = 0
        idx = len(fib) - 1
        while A > 0:
            while fib[idx] > A:
                idx -= 1
            ans += 1
            A -= fib[idx]
        return ans
            