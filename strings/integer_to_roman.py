class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman2(self, A):
        M = ['','M','MM','MMM']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        I = ['','I','II','III','IV','V','VI','VII','VIII','IX']

        return M[A//1000] + C[(A%1000)//100] + X[(A%100)//10] + I[A%10]

        
    def intToRoman(self, A):
        d = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        ans = ''
        
        if A >= 100:
            a, r = divmod(A, 1000)
            ans += d[1000] * a
            if r >= 900:
                ans += d[100] + d[1000]
                A = r - 900
            elif r >= 500:
                ans += d[500]
                A = r - 500
            elif r >= 400:
                ans += d[100] + d[500]
                A = r - 400
            else:
                A = r
        
        if A >= 10:
            a, r = divmod(A, 100)
            ans += d[100] * a
            if r >= 90:
                ans += d[10] + d[100]
                A = r - 90
            elif r >= 50:
                ans += d[50]
                A = r - 50
            elif r >= 40:
                ans += d[10] + d[50]
                A = r - 40
            else:
                A = r
        
        if A >= 1:
            a, r = divmod(A, 10)
            ans += d[10] * a
            if r >= 9:
                ans += d[1] + d[10]
                A = r - 9
            elif r >= 5:
                ans += d[5]
                A = r - 5
            elif r >= 4:
                ans += d[1] + d[5]
                A = r - 4
            else:
                A = r
                
        ans += d[1] * A
        
        return ans
      