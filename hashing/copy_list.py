# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head
            
        cur = head
        while cur:
            temp = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = temp
            cur = temp
        cur = head
        while cur:
            nxt = cur.next
            if cur.random:
                nxt.random = cur.random.next
            cur = nxt.next
        
        newhead = head.next
        cur, newcur = head, newhead
        while cur:
            cur.next = newcur.next
            if cur.next:
                newcur.next = cur.next.next
            cur = cur.next
            newcur = newcur.next
        return newhead
        
    def copyRandomList1(self, head):
        newhead = RandomListNode("dummy")    
        cur, newcur = head, newhead
        H = {}
        while cur:
            newcur.next = RandomListNode(cur.label)
            newcur = newcur.next
            H[cur] = newcur
            cur = cur.next
        newhead = newhead.next
        cur, newcur = head, newhead
        while cur:
            if cur.random:
                newcur.random = H[cur.random]
            cur, newcur = cur.next, newcur.next
        return newhead