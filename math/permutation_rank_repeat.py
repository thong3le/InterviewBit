class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n = len(A)
        rank = 1
        for i in range(n):
            sub = A[i+1:]
            counter = {}
            #print(i, sub, end=': ')
            for j in sub:
                if j in counter:
                    counter[j] += 1
                elif j <= A[i]:
                    counter[j] = 1
            #print(counter)
            for v in counter.keys():
                counter[v] -= 1
                rank = (rank + self.compute(list(counter.values()))) % 1000003
                counter[v] += 1
            #print(rank)
        return rank
    
    def compute(self, v):
        N = 1000003
        res = 1
        n = 1
        for i in range(len(v)):
            tmp1 = 1
            tmp2 = 1
            for j in range(n, n+v[i]):
                tmp1 *= j
                tmp2 *= j-n+1
            res = res * (tmp1//tmp2) % N
            n = n + v[i]
        return res

    def inverse(self, a):
        P = 11
        ans = 1
        while P > 0:
            if P % 2 == 0:
                a = ( a * a )
                P //= 2
            else:
                ans = (ans * a)
                P -= 1
        return ans

a = Solution()


print(a.inverse(3))
print(3**11)
    #print(pow(i, 1000001, 1000003))

