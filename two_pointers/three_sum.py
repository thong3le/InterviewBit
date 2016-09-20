class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        if len(A) < 3:
            return 1000000000
        A.sort()
        n = len(A)
        ans = sum(A[:3])
        mindiff = abs(ans - B)
        for i in range(n-2):
            j = i+1
            k = n - 1
            while j < k:
                temp = A[i] + A[j] + A[k]
                diff = abs(temp - B)
                if diff == 0:
                    return temp
                if diff < mindiff:
                    mindiff = diff
                    ans = temp
                if temp <= B:
                    j += 1
                else:
                    k -= 1
        return ans