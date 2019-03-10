class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, root, result):
        if root is None:
            return

        result.append(root.val)

        for node in root.children:
            self.helper(node, result)

class Solution:
    # divide conqure
    def preorder(self, root):
        if root is None:
            return []
        res = []
        res.append(root.val)
        for node in root.children:
            res += self.preorder(node)
        return res
