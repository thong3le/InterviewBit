from bisect import bisect, bisect_left

class Solution:

	def searchRange(self, A, B):
		lo = 0
		hi = len(A) - 1
		found = -1
		while lo <= hi:
			mid = (lo + hi)//2
			if A[mid] == B:
				found = mid
				hi = mid - 1
			elif A[mid] < B:
				lo = mid + 1
			else:
				hi = mid - 1
		if not found:
			return [-1,-1]

		lo = found
		hi = len(A) - 1
		found = -1
		while lo <= hi:
			mid = (lo + hi)//2
			if A[mid] == B:
				found = mid
				lo = mid + 1
			elif A[mid] < B:
				lo = mid + 1
			else:
				hi = mid - 1
		hi = found
		return [lo, hi]



	def searchRange1(self, A, B):
		l = bisect_left(A, B)
		r = bisect(A, B) - 1
		if l == len(A) or A[l] != B:
			l = -1
		if A[r] != B:
			r = -1
		return [l,r]