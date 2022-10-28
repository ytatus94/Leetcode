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
        graph = self.build_graph(org, seqs)
        indegree = self.get_indegree(org, seqs)
        topo_sort = self.bfs(graph, indegree)

        # print(graph)
        # print(indegree)
        # print(topo_sort)

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
                graph[seq[i-1]].append(seq[i])
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
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    hash_map.append(neighbor)
    
        return hash_map
