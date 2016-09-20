# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
sys.setrecursionlimit(20000)

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    
    def getSuccessor(self, A, B):
        succ = None
        node = A
        while node:
            if B == node.val:
                node = node.right
                while node:
                    succ = node
                    node = node.left
                return succ
            elif B < node.val:
                succ = node
                node = node.left
            else:
                node = node.right
        return succ
            
            
    def find(self, A, B):
        if A is None:
            return None
        if A.val == B:
            return A
        elif B < A.val:
            return self.find(A.left, B)
        else:
            return self.find(A.right, B)
            
    def getSuccessor1(self, A, B):
        node = self.find(A, B)
        if node is None:
            return None
        elif node.right:
            temp = node.right
            while temp.left:
                temp = temp.left
            return temp
        else:
            suc = None
            anc = A
            while anc != node:
                if node.val < anc.val:
                    suc = anc
                    anc = anc.left
                else:
                    anc = anc.right
            return suc