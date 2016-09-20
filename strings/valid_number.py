import re
class Solution:
    # @param A : string
    # @return an integer
            
    def isNumber(self, A):
        a = A.strip().split('e')
        if len(a) > 2 or (len(a) == 2 and not self.isInt(a[1])):
            return 0
        b = a[0].split('.')
        if len(b) > 2:
            return 0
        if len(b) == 2:
            if not b[1].isdigit():
                return 0
            if len(b[0]) == 0 or b[0] == '-' or b[0] == '+' or b[0].isdigit():
                return 1
            else:
                return self.isInt(b[0])
                
        return self.isInt(b[0])
    
    def isInt(self, a):
        if len(a) == 0:
            return False
        if len(a) == 1:
            return a.isdigit()
        if len(a) > 1:
            return (a[0] == '-' or a[0] == '+' or a[0].isdigit()) and a[1:].isdigit()
