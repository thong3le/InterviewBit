from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        n = len(A)
        ans = []
        queue = deque()
        for i in range(n):
            while queue and A[queue[-1]] < A[i]:
                queue.pop()
            queue.append(i)
            if queue[0] == i-B:
                queue.popleft()
            if i >= B-1:
                ans.append(A[queue[0]])
        return ans