class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def find(self, root, result):
        if root.left:
            self.find(root.left, result)
        result[0] -= 1
        if result[0] == 0:
            result[1] = root.val
            return
        if root.right:
            self.find(root.right, result)
        
    def kthsmallest(self, root, k):
        if root is None:
            return 0
        result = [k, -1]
        self.find(root, result)
        return result[1]