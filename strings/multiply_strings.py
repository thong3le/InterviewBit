class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        if A == '0' or B == '0':
            return '0'
        A, B = A.lstrip('0'), B.lstrip('0')
        result = '0'
        for i, c in enumerate(B[::-1]):
            temp = self.multiply_digit(A, c) + ('0'*i)
            result = self.add(result, temp)
        return result
        
    def multiply_digit(self, A, d):
        ans = []
        carry, d = 0, int(d)
        for c in A[::-1]:
            carry, r = divmod(d * int(c) + carry, 10)
            ans.append(str(r))
        if carry > 0:
            ans.append(str(carry))
        return ''.join(ans[::-1])
        
    def add(self, A1, A2):
        ans = []
        carry = 0
        if len(A2) < len(A1):
            A1, A2 = A2, A1
        A1, A2 = A1[::-1], A2[::-1]
        
        for i in range(len(A1)):
            carry, r = divmod(int(A1[i]) + int(A2[i]) + carry, 10)
            ans.append(str(r))
        
        for i in range(len(A1), len(A2)):
            carry, r = divmod(int(A2[i]) + carry, 10)
            ans.append(str(r))
        
        if carry > 0:
            ans.append(str(carry))
        return ''.join(ans[::-1])