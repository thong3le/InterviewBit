class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        lo = 1
        hi = A
        while lo <= hi:
            mid = (lo+hi)//2
            x = mid * mid
            if x == A:
                return mid
            elif x < A:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo if lo * lo < A else lo - 1