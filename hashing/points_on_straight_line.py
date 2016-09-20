from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        n = len(A)
        if n <= 2:
            return n
        m = max(Counter(A).values())
        for i in range(n):
            d = {}
            for j in range(n):
                if A[j] != A[i]:
                    k = 1.0 * (B[j] - B[i])/(A[j] - A[i])
                    d[k] = d.get(k, 1) + 1
            m = max(m, max(d.values()) if len(d) > 0 else 0)
        return m

    def gcd(self, a, b):
        return b if a == 0 else self.gcd(b%a, a)

    def maxPoints1(self, A, B):
        n = len(A)
        if n <= 2:
            return n
        m = max(Counter(A).values())
        for i in range(n):
            d = {}
            for j in range(n):
                if A[j] != A[i]:
                    dy, dx = B[j] - B[i], A[j] - A[i]
                    g = self.gcd(abs(dy), abs(dx))
                    if dy < 0:
                        dy *= -1
                        dx *= -1
                    elif dy == 0:
                        dx = abs(dx)
                    dy = dy//g
                    dx = dx//g
                    d[(dy, dx)] = d.get((dy,dx), 1) + 1
            if len(d) > 0:
                m = max(m, max(d.values()))
        return m

a = list(map(int, raw_input().strip().split()))
n = a[0]
A = []
B = []
for i in range(1, len(a)):
    if i%2:
        A.append(a[i])
    else:
        B.append(a[i])
print(len(A), len(B))
print(Solution().maxPoints1(A, B))