class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        A = A.strip()
        if len(A) == 0 or not (A[0] in ['-', '+'] or A[0].isdigit()):
            return 0
        neg = False
        if A[0] in  ['-','+']:
            neg = True if A[0] == '-' else False
            A = A[1:]
        D = []
        for c in A:
            if c.isdigit():
                D.append(c)
            else:
                break
        ans = 0
        for i, c in enumerate(D[::-1]):
            ans += int(c) * 10**i
        ans = -ans if neg else ans
        if ans > INT_MAX or ans < INT_MIN:
            return INT_MIN if neg else INT_MAX
        return ans