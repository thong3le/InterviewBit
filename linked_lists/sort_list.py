# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if A is None or A.next is None:
            return A
        h1 = A
        h2 = A.next
        while h2 and h2.next:
            h1 = h1.next
            h2 = h2.next.next
        h2 = h1.next
        h1.next = None
        return self.merge(self.sortList(A), self.sortList(h2))
    
    def merge(self, h1, h2):
        if h1 is None or h2 is None:
            return h1 or h2
        head = ListNode(0)
        cur = head
        cur1, cur2 = h1, h2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        cur.next = cur1 or cur2
        return head.next