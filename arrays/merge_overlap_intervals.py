# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0:
            return intervals
        intervals.sort(key = lambda x: x.start)
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            s1, e1 = stack[-1].start, stack[-1].end
            s2, e2 = intervals[i].start, intervals[i].end
            if s2 > e1:
                stack.append(intervals[i])
            elif s2 <= e1 <= e2:
                stack.pop()
                stack.append(Interval(s1, e2))
            else:
                continue
        return stack