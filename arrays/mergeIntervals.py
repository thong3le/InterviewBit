# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return str((self.start, self.end))

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        lo = 0
        hi = len(intervals)
        while lo < hi:
            mid = (lo + hi)//2
            if intervals[mid].start == new_interval.start:
                lo = hi = mid
            elif intervals[mid].start < new_interval.start:
                lo = mid + 1
            else:
                hi = mid

        intervals.insert(lo, new_interval)
        stack = [intervals[0]]
        
        for i in range(1, len(intervals)):
            s1, e1 = stack[-1].start, stack[-1].end
            s2, e2 = intervals[i].start, intervals[i].end
            if e1 < s2:
                stack.append(intervals[i])
            elif s2 <= e1 <= e2:
                stack.pop()
                stack.append(Interval(s1, e2))
        return stack

s = Solution()

intervals = [Interval(3,6), Interval(8,10)]
new_interval = Interval(1,2)

res = s.insert(intervals, new_interval)

for i in res:
    print(i)