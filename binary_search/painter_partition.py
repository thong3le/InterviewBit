class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        lo = max(C)
        hi = sum(C)
        while lo < hi:
            mid = (lo + hi)//2
            if self.ispossible(C, mid, A):
                hi = mid
            else:
                lo = mid + 1
        return (lo * B) % 10000003

    def ispossible(self, C, mid, A):
        count, total = 1, 0
        for n in C:
            total += n
            if total > mid:
                total = n
                count += 1
        return count <= A