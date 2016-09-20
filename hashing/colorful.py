class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = list(map(int, str(A)))
        n = len(A)
        products = set()
        for i in range(n):
            p = 1
            for j in range(i, n):
                p *= A[j]
                if p in products:
                    return 0
                else:
                    products.add(p)
        print(products)
        return 1

print(Solution().colorful(99))