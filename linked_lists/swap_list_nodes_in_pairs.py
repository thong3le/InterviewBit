# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        head = ListNode(0)
        head.next = A
        cur = head
        while cur.next and cur.next.next:
            c1 = cur.next
            c2 = c1.next
            h = c2.next
            cur.next = c2
            c2.next = c1
            c1.next = h
            cur = c1
        return head.next
            