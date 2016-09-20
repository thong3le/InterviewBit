class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        indent = 0
        result = []
        cur = ''
        for i in range(len(A)):
            if A[i] == '[' or A[i] == '{':
                if cur:
                    result.append('\t'*indent + cur)
                cur = ''
                result.append('\t'*indent + A[i])
                indent += 1
            elif A[i] == ']' or A[i] == '}':
                if cur:
                    result.append('\t'*indent + cur)
                cur = ''
                indent -= 1
                result.append('\t'*indent + A[i])
            elif A[i] == ',':
                if cur:
                    result.append('\t'*indent + cur + A[i])
                else:
                    result[-1] += A[i]
                cur = ''
            else:
                cur += A[i]
        return result