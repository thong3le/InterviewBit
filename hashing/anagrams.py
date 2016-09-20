class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        d = {}
        for i in range(len(A)):
            w = ''.join(sorted(A[i]))
            if w in d:
                d[w].append(i+1)
            else:
                d[w] = [i+1]
        
        return sorted(list(d.values()))

S = Solution()
print()