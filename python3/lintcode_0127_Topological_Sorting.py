# lintcode 127
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if graph is None:
            return []
            
        # 計算 indegree
        indegree = self.get_indegree(graph)
        
        # 用 BFS 來做拓樸排序
        queue = [] # 是要被刪掉的點 (indegree=0 的點會被 pop 出來，相當於從 graph 中刪掉了)
        order = []
        # 把所有 indegree = 0 的點當起點放到 queue 裡面
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)
                order.append(node)
                
        while queue:
            n = queue.pop(0)
            for neighbor in n.neighbors:
                # 因為把 n pop 出來了，所以 n 的每個鄰居的 indegree 都要減一
                indegree[neighbor] = indegree[neighbor] - 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    order.append(neighbor)
                    
        # 長度一樣的話代表 graph 中的每個點都有排到序
        if len(order) == len(graph):
            return order
        
        return None
        
    def get_indegree(self, graph):
        indegree = dict()
        for node in graph:
            indegree[node] = 0 # 先初始化每個點的 indegree 為 0
            
        for node in graph:
            for neighbor in node.neighbors:
                # node 的每個鄰居，都有一條由 node 指向它的邊
                indegree[neighbor] = indegree[neighbor] + 1
                
        return indegree
 
class Solution:
    # 把函數包裝起來，讓主函數變得簡潔
    def topSort(self, graph):
        if graph is None:
            return []
        # 計算每個點的 indegree
        indegree = self.get_indegree(graph)
        # 找起點 (所有 indegree = 0 的點)
        start_nodes = self.get_start_nodes(graph, indegree)
        # 用 BFS 找出拓樸排序
        order = self.bfs(start_nodes, indegree)
        
        if len(order) == len(graph):
            return order
            
        return None
        
    def get_start_nodes(self, graph, indegree):
        # nodes = []
        
        # for node in graph:
        #     if indegree[node] == 0:
        #         nodes.append(node)
                
        # return nodes
        return [node for node in graph if indegree[node] == 0]
        
    def bfs(self, start_nodes, indegree):
        queue = []
        order = []
        
        # 把所有起點放到 queue 裡面
        # hash map 要跟 queue 同步處理
        for node in start_nodes:
            queue.append(node)
            order.append(node)
            
        while queue:
            n = queue.pop(0)
            for neighbor in n.neighbors:
                indegree[neighbor] = indegree[neighbor] - 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    order.append(neighbor)
                    
        return order

