class Solution:
	def hotel(self, arrive, depart, K):
		A = [(e, 1) for e in arrive]
		B = [(e, 0) for e in depart]
		points = A + B
		points.sort()
		k = 0
		for p in points:
			k = k+1 if p[1] == 1 else k-1
			if k > K:
				return 0
		return 1


sol = Solution()
a = [1, 2, 3]
b = [2, 3, 4]
print(sol.hotel(a,b,3))
