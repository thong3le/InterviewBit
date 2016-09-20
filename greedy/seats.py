class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        ans = 0
        A = A.strip('.')
        i, j = 0, len(A) - 1
        left, right = 0, 0
        while i <= j:
            if A[i] == 'x':
                left += 1
                i += 1
            elif A[j] == 'x':
                right += 1
                j -= 1
            else:
                move, side = 0, 0
                if left <= right:
                    side = left
                    while A[i] == '.':
                        i += 1
                        move += 1
                else:
                    side = right
                    while A[j] == '.':
                        j -= 1
                        move +=1 
                ans = (ans + side * move) % 10000003
        return ans
                