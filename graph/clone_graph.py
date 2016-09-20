# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    
    def cloneGraph1(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        dic = {node: root}
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for v in node.neighbors:
                if v not in dic:
                    queue.append(v)
                    dic[v] = UndirectedGraphNode(v.label)
                dic[node].neighbors.append(dic[v])
        return root
                
            
    def cloneGraph(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        stack = [node]
        visit = {node: root}
        while stack:
            v = stack.pop()
            for w in v.neighbors:
                if w not in visit:
                    stack.append(w)
                    visit[w] = UndirectedGraphNode(w.label)
                visit[v].neighbors.append(visit[w])
        return root