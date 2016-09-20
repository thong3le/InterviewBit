# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if A is None:
            return A
        n = 1
        tail = A
        while tail.next:
            tail = tail.next
            n += 1
        B %= n
        if B == 0 or n == 1:
            return A
        tail = A
        for _ in range(B):
            tail = tail.next
        cur = A
        while tail.next:
            cur, tail = cur.next, tail.next
        tail.next = A
        A = cur.next
        cur.next = None
        return A
        