import random
class Solution:
	def maximumGap2(self, A):
		n = len(A)
		d = 0
		for i in range(n):
			for j in range(n-1, i, -1):
				if A[i] <= A[j]:
					d = max(j-i, d)
		return d

	def maximumGap1(self, A):
		n = len(A)
		d = 0
		B = [(A[i], i) for i in range(n)]
		B.sort()
		Rmax_index = [0] * n
		Rmax_index[n-1] = B[n-1][1]
		for i in range(n-2, -1, -1):
			Rmax_index[i] = max(Rmax_index[i+1], B[i][1])
		for i in range(n-1):
			d = max(Rmax_index[i+1] - B[i][1], d)
		return d
	
	def maximumGap(self, A):
		n = len(A)
		d = 0
		Lmin = [0] * n
		Rmax = [0] * n
		Lmin[0] = A[0]
		Rmax[n-1] = A[n-1]

		for i in range(1, n):
			Lmin[i] = min(Lmin[i-1], A[i])
		for i in range(n-2, -1, -1):
			Rmax[i] = max(Rmax[i+1], A[i])

		i = j = 0
		while i < n and j < n:
			if Lmin[i] <= Rmax[j]:
				d = max(j-i, d)
				j += 1
			else:
				i += 1

		return d


s = Solution()
a = [random.randint(1, 10) for _ in range(7)]
print(a)
print(s.maximumGap(a))