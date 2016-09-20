# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A is None or A.next is None:
            return None
        slow, fast = A.next, A.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow != fast:
            return None
        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow