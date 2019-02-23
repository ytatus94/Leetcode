"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        # 先一路指回 root 然後把所有節點記錄下來
        paths_a = self.get_paths_to_root(A)
        paths_b = self.get_paths_to_root(B)
        
        # 取得 paths 中 root 的 index
        # root 是 paths 裡面的最後一個節點
        index_a = len(paths_a) - 1
        index_b = len(paths_b) - 1
        
        # 從 root 開始一路往回看
        lca = None
        while index_a >= 0 and index_b >= 0:
            if paths_a[index_a] != paths_b[index_b]:
                break
            lca = paths_a[index_a] # 如果兩個相等，那就是公共祖先
            index_a -= 1
            index_b -= 1
            
        return lca

    def get_paths_to_root(self, node):
        paths = []
        while node is not None:
            paths.append(node)
            node = node.parent
        
        return paths
