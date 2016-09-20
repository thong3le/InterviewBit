# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        curA, curB = A, B
        while curA != curB:
            curA = B if curA is None else curA.next
            curB = A if curB is None else curB.next
        return curA