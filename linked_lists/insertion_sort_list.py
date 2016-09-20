# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        a = []
        cur = A
        while cur:
            a.append(cur.val)
            cur = cur.next
        a.sort()
        cur = A
        for e in a:
            cur.val = e
            cur = cur.next
        return A