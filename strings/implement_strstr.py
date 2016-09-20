class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr1(self, haystack, needle):
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        n, k = len(haystack), len(needle)
        for i in range(n-k+1):
            if haystack[i:i+k] == needle:
                return i
        return -1
    def strStr(self, haystack, needle):
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        else:
            return haystack.find(needle)