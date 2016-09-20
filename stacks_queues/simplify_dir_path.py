class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        stack = []
        for d in A.split('/'):
            if len(d) == 0 or d == '.':
                continue
            elif d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/' + '/'.join(stack)