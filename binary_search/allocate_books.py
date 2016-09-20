class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B > len(A):
            return -1
        lo, hi = max(A), sum(A)
        while lo < hi:
            mid = (lo + hi)//2
            if self.require_students(A, mid) <= B:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def require_students(self, A, mid):
        count, total = 1, 0
        for p in A:
            total += p
            if total > mid:
                total = p
                count += 1
        return count