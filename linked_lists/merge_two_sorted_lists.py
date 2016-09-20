# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A is None or B is None:
            return A or B
        head = A if A.val <= B.val else B
        curA, curB = A, B
        while curA and curB:
            if curA.val <= curB.val:
                if curA.next is None: 
                    curA.next = curB
                    return head
                if curA.next.val <= curB.val:
                    curA = curA.next
                else:
                    tmp = curA.next
                    curA.next = curB
            else:
                curA, curB = curB, curA