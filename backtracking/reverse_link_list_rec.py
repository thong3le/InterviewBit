# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if A is None or A.next is None:
            return A
        head = self.reverseList(A.next)
        B = A.next
        B.next = A
        A.next = None
        return head