def sort(A, lo = 0, hi = None):
    if hi is None:
        hi = len(A) - 1
    if lo == hi:
        return
    mid = (lo + hi)//2
    sort(A, lo, mid)
    sort(A, mid+1, hi)
    merge(A, lo, mid+1, hi)

def merge(A, lo, mid, hi):
    i, j = lo, mid
    temp = []
    while i <= mid-1 and j <= hi:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    temp.extend(A[i:mid] + A[j:hi+1])
    for i in range(lo, hi+1):
        A[i] = temp[i-lo]

def count_inversions(A, lo = 0, hi = None):
    if hi is None:
        hi = len(A) - 1
    if lo == hi:
        return 0
    mid = (lo + hi)//2
    ans = count_inversions(A, lo, mid)
    ans += count_inversions(A, mid+1, hi)
    ans += merge_and_count(A, lo, mid+1, hi)
    return ans

def merge_and_count(A, lo, mid, hi):
    i, j = lo, mid
    count = 0
    temp = []
    while i <= mid-1 and j <= hi:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            count += mid - i
            temp.append(A[j])
            j += 1
    temp.extend(A[i:mid])
    temp.extend(A[j:hi+1])
    for i in range(lo, hi+1):
        A[i] = temp[i-lo]
    return count


        
A = [ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ]

sort(A)
print(A)

print(count_inversions(A))