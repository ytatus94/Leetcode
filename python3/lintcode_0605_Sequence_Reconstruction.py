# 這題和 course schedule i, course schedule ii 一樣，都是用標準的 topological sorting 模板
# 要注意的地方是，因為 org 的排序要唯一，那每個 loop 的 queue 只能有一個數，不然無法唯一
# 例如: 開始的時候 queue=[1], hash_map=[1], 可是第二圈的時候如果 queue=[2,3]
# 那加入 hash_map 後可以是 [1,2,3] 或 [1,3,2] 雖然滿足 topological sorting 的要求，但是就是不唯一的了

from typing import (
    List,
)

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # write your code here
        # 先檢查 org 和 seqs 的點有沒有 match
        # 若某個點 org 有 seqs 沒有 --> False
        # 若某個點 org 沒有 seqs 有 --> False
        all_nodes = [i for seq in seqs for i in seq]
        if set(org) != set(all_nodes):
            return False

        # 要判斷是否能從 seqs 組成唯一的一組 org，所以建立 graph 和 indegree 時，就用 org 來建立就好
        # 如果 seqs 中存在 org 中沒有存在的點，那就是 False 因為照題目的要求會用到 seqs 中的每個點
        graph = self.build_graph(org, seqs) # 1. 建立圖
        indegree = self.get_indegree(org, seqs) # 2. 統計所有的 indegree
        topo_sort = self.bfs(graph, indegree)

        # 如果長度不一樣，seqs 就不可能重組成 org
        if len(topo_sort) != len(org):
            return False

        # 長度一樣了，就要比較 list 內的元素
        for i in range(len(org)):
            if topo_sort[i] != org[i]:
                return False

        return True

    def build_graph(self, org, seqs):
        graph = {x: [] for x in org}
        # seqs 的其中一個元素可能是 [xi, xi+1, xi+2, ..., xi+n]
        # 表示 xi 要在其他元素之前，xi+1 要在 i+2 到 i+n 元素之前，以此類推
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i-1]].append(seq[i]) # 只要紀錄 xi 要排在 xi+1 前面就好
        return graph

    def get_indegree(self, org, seqs):
        indegree = {x: 0 for x in org}
        for seq in seqs:
            for i in range(len(seq) - 1):
                indegree[seq[i+1]] += 1
        return indegree

    def bfs(self, graph, indegree):
        queue = [k for k, v in indegree.items() if v == 0]
        hash_map = [k for k, v in indegree.items() if v == 0]

        while queue:
            if len(queue) > 1:
                return []
            n = queue.pop(0)
            for neighbor in graph[n]:
                indegree[neighbor] -= 1 # 從 queue 中把點跳出來，把這個點的鄰居的 indegree 減一
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    hash_map.append(neighbor)
    
        return hash_map
