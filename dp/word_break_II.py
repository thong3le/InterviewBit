class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):
        n = len(A)
        d = set(B)
        result = [[] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(i):
                if A[j:i] in d:
                    if j == 0:
                        result[i].extend([A[j:i]])
                    else:
                        result[i].extend([e + ' ' + A[j:i] for e in result[j]])
        return sorted(result[n])
        
        

A = "aabbbabaaabbbabaabaab"
B = [ "bababbbb", "bbbabaa", "abbb", "a", "aabbaab", "b", "babaabbbb", "aa", "bb" ]

s = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]

print(Solution().wordBreak(s,d))
