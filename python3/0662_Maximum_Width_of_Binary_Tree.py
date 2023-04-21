# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # 把每一個節點標記 index 這樣就能用每一層的最右邊的點的 index 減去
        # 最左邊的點的 index 來獲得 width
        # 再打擂台得到 max_width

        max_width = 0
        queue = [(root, 0)] # 第一個節點的 index 設為 0

        while queue:
            # 進到每一層時，找出最左邊和最右邊的點的 index 就能計算長度
            left_most_node, left_idx = queue[0]
            right_most_node, right_idx = queue[-1]
            max_width = max(max_width, right_idx - left_idx + 1)

            # 把下一層的節點加入到 queue 裡面
            # 左子樹節點 index = 2 * 當前節點 index + 1
            # 右子樹節點 index = 2 * 當前節點 index + 2
            # 結點的 index 的公式可以由畫圖歸納出來
            for i in range(len(queue)):
                node, idx = queue.pop(0)
                if node.left is not None:
                    queue.append((node.left, 2 * idx + 1))
                if node.right is not None:
                    queue.append((node.right, 2 * idx + 2))

        return max_width
                

