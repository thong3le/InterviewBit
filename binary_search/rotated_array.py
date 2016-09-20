class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        n = len(A)
        lo = 0
        hi = len(A) - 1
        while lo <= hi:
            if A[lo] <= A[hi]: return A[lo]
            mid = (lo + hi)//2
            pre = (mid-1+n)%n
            nxt = (mid+1)%n
            if A[mid] <= A[nxt] and A[mid] <= A[pre]:
                return A[mid]
            elif A[mid] <= A[hi]: hi = mid - 1
            elif A[mid] >= A[lo]: lo = mid + 1
        return -1