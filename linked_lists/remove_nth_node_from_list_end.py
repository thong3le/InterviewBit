# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if A is None or B <= 0:
            return A
        tail = A
        for _ in range(B):
            if tail: tail = tail.next
            if tail is None:
                return A.next
        cur = A
        while tail.next:
            cur, tail = cur.next, tail.next
        cur.next = cur.next.next
        return A