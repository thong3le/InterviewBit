class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def gcd(self, a, b):
        return b if a == 0 else self.gcd(b%a, a)
        
    def fractionToDecimal(self, n, d):
        sign = '-' if n * d < 0 else ''
        n, d = abs(n), abs(d)
        a = self.gcd(n,d)
        n, d = n//a, d//a
        x, r = divmod(n, d)
        if r == 0:
            return sign + str(x)
        ans = str(x) + '.'
        u = set()
        s = []
        while r != 0 and r not in u:
            u.add(r)
            x, r = divmod(10*r, d)
            s.append(str(x))

        if r != 0:
            x = 10*r//d
            i = s.index(str(x))
            return sign + ans + ''.join(s[:i]) + '(' + ''.join(s[i:]) + ')'
        return sign + ans + ''.join(s)

    def fractionToDecimal1(self, n, d):
        sign = '-' if n * d < 0 else ''
        n, d = abs(n), abs(d)
        a = self.gcd(n,d)
        n, d = n//a, d//a
        x, r = divmod(n, d)
        if r == 0:
            return sign + str(x)
        ans = sign + str(x) + '.'
        u = {}
        s = []
        index = 0
        while r != 0 and r not in u:
            u[r] = index
            x, r = divmod(10*r, d)
            s.append(str(x))
            index += 1
        return ans + ''.join(s) if r == 0 else ans + ''.join(s[:u[r]]) + '(' + ''.join(s[u[r]:]) + ')'

a = 122
b = 250
print(a*1.0/b)
print(Solution().fractionToDecimal(a, b))