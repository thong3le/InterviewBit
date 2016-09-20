from collections import Counter
class Solution:
    # @param S : string
    # @param T : string
    # @return a string
    def minWindow(self, S, T):
        counts = Counter(T)
        l, r = 0,0
        length = 0
        total = 0
        i = 0
        
        for j in range(len(S)):
            if S[j] not in counts:
                continue
            counts[S[j]] -= 1
            if counts[S[j]] >= 0:
                total += 1
            if total == len(counts):
                while S[i] not in counts or counts[S[i]] < 0:
                    if S[i] in counts:
                        counts[S[i]] += 1
                    i += 1
                    
                if  length == 0 or j-i+1 < length:
                    length = j-i+1
                    l, r = i, j
        return S[l:r+1] if length != 0 else ''