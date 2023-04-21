class Solution:
  def levelSum(self, root, level):
        result = []
        self.dfs(root, 1, result, level)
        return sum(p)

    def dfs(self, root, curr_level, result, target_level):
        if root is None:
            return

        if curr_level == target_level:
            result.append(root.val)

        self.dfs(root.left, curr_level + 1, result, target_level)
        self.dfs(root.right, curr_level + 1, result, target_level)
