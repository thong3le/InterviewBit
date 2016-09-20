import math
class RSQ:
	def __init__(self, A):
		self.size = 1 << int(math.ceil(math.log(len(A), 2)))
		self.data = [0] * 2 * self.size
		for i in range(len(A)):
			self.add(i, A[i])

	def add(self, pos, x):
		pos += self.size
		while pos > 0:
			self.data[pos] += x
			pos //= 2
	def sum(self, lo, hi):
		lo = self.size if lo <= 0 else lo + self.size
		hi = 2*self.size if hi > self.size else hi + self.size
		ans = 0
		while lo < hi:
			if lo & 1:
				ans += self.data[lo]
				lo += 1
			if hi & 1:
				hi -= 1
				ans += self.data[hi]
			lo //= 2
			hi //= 2
		return ans

a = [1,2,3,4,5,6,7,8,9,10]
d = RSQ(a)
print(d.sum(3,6))
