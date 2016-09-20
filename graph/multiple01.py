from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        M = [None] * A
        queue = deque([1])
        while queue:
            #print(queue)
            x = queue.popleft()
            if x % A == 0:
                ans = []
                while x != 1:
                    x, b = M[x]
                    ans.append(b)
                ans.append('1')
                return ''.join(ans[::-1])
            left, right = (10*x)%A, (10*x+1)%A
            if M[left] is None:
                M[left] = (x, '0')
                queue.append(left)
            if M[right] is None:
                M[right] = (x, '1')
                queue.append(right)
        return -1


print(Solution().multiple(9345711))