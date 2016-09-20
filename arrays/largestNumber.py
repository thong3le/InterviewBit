class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        a = [str(n) for n in A]
        a.sort(cmp = lambda x,y: 0 if x+y == y+x else -1 if x+y > y+x else 1)
        return ''.join(a)

a = Solution()
print(a.largestNumber([3,30,300,3000]))