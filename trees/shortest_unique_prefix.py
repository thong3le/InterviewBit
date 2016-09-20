class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.prefixes = 0
        
class Solution:
    # @param A : list of strings
    # @return a list of strings
    def add(self, root, w):
        n = len(w)
        cur = root
        for i in range(n):
            cur.prefixes += 1
            index = ord(w[i]) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.prefixes += 1
    
    def shortest_unique_prefix(self, root, w):
        n = len(w)
        cur = root
        for i in range(n):
            index = ord(w[i]) - ord('a')
            if cur.prefixes == 1:
                return w[:i]
            cur = cur.children[index]
        return w
    
    def prefix(self, A):
        result = []
        root = TrieNode()
        for w in A:
            self.add(root, w.lower())
        for w in A:
            result.append(self.shortest_unique_prefix(root, w.lower()))
        return result