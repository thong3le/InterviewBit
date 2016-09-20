import sys
#sys.setrecursionlimit(20000)

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.space = end - start
        self.left = None
        self.right = None

def build_tree(root):
    start, end = root.start, root. end
    if end - start <= 1:
        return 
    mid = (start + end)//2
    root.left = Node(start, mid)
    root.right = Node(mid, end)
    build_tree(root.left)
    build_tree(root.right)

def find(root, i):
    root.space -= 1
    if root.left == None:
        return root.start
    if root.left.space > i:
        return find(root.left, i)
    return find(root.right, i - root.left.space)

class Solution:
	# @param heights : list of integers
	# @param infronts : list of integers
	# @return a list of integers
	def order(self, H, P):
	    root = Node(0, len(H))
	    build_tree(root)
	    ans = [0] * len(H)
	    for h, p in sorted(zip(H, P)):
	        i = find(root, p)
	        ans[i] = h
	    return ans
	        
	def order1(self, heights, infronts):
	    n = len(heights)
	    d = {}
	    for i in range(n):
	        d[heights[i]] = infronts[i]
	    heights.sort()
	    ans = [0]*n
	    pos = list(range(n))
	    for h in heights:
	        ans[pos[d[h]]] = h
	        pos.pop(d[h])
	    return ans 