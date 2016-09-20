from bisect import bisect_left, bisect_right
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        n = len(A)
        lo, hi = 0, n-1
        ans = [-1,-1]
        while lo < hi:
            mid = lo + (hi-lo)//2
            if A[mid] < B: lo = mid + 1
            else: hi = mid
        if A[lo] != B:
            return ans
        ans[0] = lo
        hi = n-1
        while lo < hi:
            mid = lo + (hi-lo)//2 + 1
            if A[mid] > B: hi = mid - 1
            else: lo = mid
        ans[1] = hi
        return ans
        
                
    def searchRange1(self, A, B):
        l = bisect_left(A, B)
        r = bisect_right(A, B) - 1
        if l < len(A) and A[l] != B:    l = -1
        if A[r] != B:   r = -1
        return [l,r]
