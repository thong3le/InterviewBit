class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        if m == 0:
            if n % 2 == 0:
                return (B[n//2-1] + B[n//2]) / 2.0
            else:
                return B[n//2]
                
        loA, hiA = 0, m
        half = (m+n+1)//2
        while loA <= hiA:
            midA = (loA + hiA)//2
            midB = half - midA
            if midB > 0 and midA < m and B[midB - 1] > A[midA]:
                loA = midA + 1
            elif midA > 0 and midB < n and A[midA-1] > B[midB]:
                hiA = midA - 1
            else:
                if midA == 0: max_left = B[midB - 1]
                elif midB == 0: max_left = A[midA-1]
                else: max_left = max(A[midA-1], B[midB-1])
                
                if (m+n) % 2 == 1:
                    return max_left
                
                if midA == m : min_right = B[midB]
                elif midB == n: min_right = A[midA]
                else: min_right = min(A[midA], B[midB])
                
                return (max_left + min_right) / 2.0
