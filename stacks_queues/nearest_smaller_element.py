class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        ans = []
        stack = []
        for i in range(0, len(arr)):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(arr[i])
        return ans