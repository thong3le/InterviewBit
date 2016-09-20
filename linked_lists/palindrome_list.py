# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, head):
        if head is None:
            return 1
        stack = []
        slow, fast = head, head
        while fast and fast.next:
            stack.append(slow.val)
            slow, fast = slow.next, fast.next.next
        if fast:
            slow = slow.next
        while stack:
            if stack.pop() != slow.val:
                return 0
            else:
                slow = slow.next
        return 1