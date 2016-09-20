from collections import deque, defaultdict
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        words = set(dictV)
        words.add(end)
        parents = defaultdict(list)
        dist = defaultdict(int)
        queue = deque([start])
        dist[start] = 1
        while queue:
            node = queue.popleft()
            for j in range(len(node)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if node[j] != c:
                        newnode = node[:j] + c + node[j+1:]
                        if newnode in words:
                            if dist[newnode] == 0:
                                dist[newnode] = dist[node] + 1
                                queue.append(newnode)
                                parents[newnode].append(node)
                            elif dist[newnode] == dist[node] + 1:
                                parents[newnode].append(node)
        result = []
        def backtrack(p):
            if p[-1] == start:
                result.append(p[::-1])
            else:
                for w in parents[p[-1]]:
                    backtrack(p + [w])
        backtrack([end])
        return result