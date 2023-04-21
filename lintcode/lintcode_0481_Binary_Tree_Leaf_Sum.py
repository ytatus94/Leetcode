def leafSum(self, root):
        result = []
        self.dfs(root, result)
        return sum(result)

    def dfs(self, root, result):
        if root is None:
            return

        if root.left is None and root.right is None:
            result.append(root.val)

        self.dfs(root.left, result)
        self.dfs(root.right, result)
