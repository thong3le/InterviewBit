class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n = len(A)
        MOD = 1000003
        
        fac = [1] * (n+1)
        for i in range(1, n+1):
            fac[i] = (fac[i-1] * i) % MOD
        
        chars = [0] * 256
        for c in A:
            chars[ord(c)] += 1
            
        rank = 1
        for i in range(n):
            for j in range(ord(A[i])):
                if chars[j] == 0: continue
                num_perm = fac[n-1-i]
                chars[j] -= 1
                for k in range(256):
                    if chars[k] <= 1: continue
                    num_perm = (num_perm * self.inverse(fac[chars[k]])) % MOD
                chars[j] += 1
                rank = (rank + num_perm) % MOD
            
            chars[ord(A[i])] -= 1
            
        return rank
    
    def inverse(self, a):
        MOD = 1000003
        P = MOD - 2
        ans = 1
        while P > 0:
            if P % 2 == 0:
                a = ( a * a ) % MOD
                P //= 2
            else:
                ans = (ans * a) % MOD
                P -= 1
        return ans