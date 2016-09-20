from collections import deque
class Solution:
	# @param N : integer
	# @param M : integer
	# @param x1 : integer
	# @param y1 : integer
	# @param x2 : integer
	# @param y2 : integer
	# @return an integer
	def knight(self, N, M, x1, y1, x2, y2):
	    X = [-2, -2, -1, -1, 1, 1, 2, 2]
	    Y = [-1, 1, -2, 2, -2, 2, -1, 1]
	    queue = deque([(x1,y1)])
	    visited = set([(x1, y1)])
	    layer = 0
	    while queue:
	        n = len(queue)
	        for _ in range(n):
	            x, y = queue.popleft()
	            if (x,y) == (x2,y2):
	                return layer
	            for i in range(8):
	                if 1 <= x + X[i] <= N and 1 <= y + Y[i] <= M and (x+X[i], y+Y[i]) not in visited:
	                    queue.append((x+X[i], y+Y[i]))
	                    visited.add((x+X[i], y+Y[i]))
	        layer += 1
	    return -1
	       