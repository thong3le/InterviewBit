# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq as pq

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        head = ListNode(0)
        cur = head
        heap = []
        for node in A:
            pq.heappush(heap, (node.val, node))
        while heap:
            x, node = pq.heappop(heap)
            if node.next:
                pq.heappush(heap, (node.next.val, node.next))
            cur.next = node
            cur = cur.next
        return head.next