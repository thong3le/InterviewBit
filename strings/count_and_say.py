class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A <= 0:
            return ''
        ans = '1'
        for i in range(A-1):
            chars = list(ans)
            c, count = chars[0], 1
            ans = []
            for i in range(1, len(chars)):
                if chars[i] == c:
                    count += 1
                else:
                    ans.extend([str(count), c])
                    c, count = chars[i], 1
            ans.extend([str(count), c])
            ans = ''.join(ans)
        return ans