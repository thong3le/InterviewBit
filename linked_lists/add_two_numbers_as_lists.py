# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if A is None or B is None:
            return A or B
        head, carry = ListNode(0), 0
        cur, curA, curB = head, A, B
        while curA and curB:
            carry, val = divmod(curA.val + curB.val + carry, 10)
            cur.next = ListNode(val)
            curA, curB, cur = curA.next, curB.next, cur.next
        curA = curA or curB
        while curA:
            carry, val = divmod(curA.val + carry, 10)
            cur.next = ListNode(val)
            curA, cur = curA.next, cur.next
        if carry != 0:
            cur.next = ListNode(carry)
        return head.next