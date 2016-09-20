from collections import deque
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        words = set(dictV)
        words.add(end)
        queue = deque([(start, 1)])
        while queue:
            node, d = queue.popleft()
            if node == end:
                return d
            for j in range(len(node)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != node[j]:
                        newnode = node[:j] + c + node[j+1:]
                        if newnode in words:
                            queue.append((newnode, d+1))
                            words.remove(newnode)
        return 0