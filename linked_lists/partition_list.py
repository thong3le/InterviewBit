# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        if A is None:
            return A
        head = ListNode(0)
        less = head
        while A and A.val < B:
            less.next = A
            A = A.next
            less.next.next = None
            less = less.next
        cur = A
        while cur and cur.next:
            if cur.next.val < B:
                less.next = cur.next
                cur.next = cur.next.next
                less.next.next = None
                less = less.next
            else:
                cur = cur.next
        less.next = A
        return head.next