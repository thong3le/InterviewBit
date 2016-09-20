# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        head = ListNode('dummy')
        head.next = A
        prev = head
        for _ in range(m-1):
            prev = prev.next
        h = prev.next
        cur = None
        nxt = h
        for _ in range(n-m+1):
            temp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = temp
        prev.next = cur
        h.next = nxt
        return head.next