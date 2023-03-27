from lintcode import (
    UndirectedGraphNode,
)

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        # write your code here
        if node is None:
            return None

        # 用 BSF 找出所有的點
        queue = [node]
        all_nodes = [node]
        while queue:
            n = queue.pop(0)
            for next_node in n.neighbors:
                # 圖可能會有 loop 所以要避免 loop
                if next_node not in all_nodes:
                    queue.append(next_node)
                    all_nodes.append(next_node)

        # 拷貝所有的點
        new_all_nodes = {}
        for n in all_nodes:
            new_node = UndirectedGraphNode(n.label)
            new_all_nodes[n] = new_node # 新舊的點要保留對應關係

        # 拷貝所有的邊
        for n in all_nodes:
            new_node = new_all_nodes[n]
            for neighbor in n.neighbors:
                neighbor_of_new_nodes = new_all_nodes[neighbor]
                new_node.neighbors.append(neighbor_of_new_nodes)

        return new_all_nodes[node]
