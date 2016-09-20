class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if not A:
            return -1
        start = 0; end = len(A)-1
        while start + 1 < end:
            mid = (start+end)/2
            if A[mid] == B:
                return mid
            if A[start] <= B < A[mid]: 
                end = mid
            elif A[mid] < B <= A[end]:
                start = mid
            elif A[mid] > A[end]:
                start = mid
            else:
                end = mid 
        if A[start] == B:return start
        elif A[end] == B:return end
        return -1