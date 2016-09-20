# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        n = 0
        cur = A
        while cur:
            n += 1
            cur = cur.next
        return self.build(A, 0, n-1)
        
    def build(self, head, i, j):
        if i > j:
            return None
        if i == j:
            return TreeNode(head.val)
        mid = (i+j)//2
        cur = head
        for _ in range(mid-i):
            cur = cur.next
        root = TreeNode(cur.val)
        root.left = self.build(head, i, mid-1)
        root.right = self.build(cur.next, mid+1, j)
        return root
        