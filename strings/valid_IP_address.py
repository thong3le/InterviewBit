class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def restore(current, start, limit):
            if limit == 0:
                if (start == len(current)-1 or current[start] != '0') and int(''.join(current[start:])) <= 255:
                    result.append(''.join(current))
            else:
                for i in range(start+1, start+4):
                    if i < len(current) and int(''.join(current[start:i])) <= 255:
                        current.insert(i, '.')
                        restore(current, i+1, limit-1)
                        del current[i]
                        if current[start] == '0': break

        result = []
        restore(list(s), 0, 3)
        return result
        
        
    def restoreIpAddresses1(self, A):
        res = self.IP(A)
        return ['.'.join(r) for r in res] if res else []
        
    def IP(self, A, p = 4):
        if len(A) == 0:
            return None
        if p == 1:
            if len(A) > 3 or int(A) > 255 or (int(A) == 0 and len(A) > 1):
                return None
            else:
                return [[A]]
        res = []
        if A[0] == '0':
            temp = self.IP(A[1:], p-1)
            if temp:
                return [['0']+t for t in temp]
                
        n = min(len(A), 3)
        for i in range(1, n+1):
            x = int(A[:i])
            if x > 255:  continue
            temp = self.IP(A[i:], p-1)
            if temp:
                for t in temp:
                    res.append([str(x)]+t)
        return res
        