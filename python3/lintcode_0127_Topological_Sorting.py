# 拓樸排序:
# 對於一個有向圖 G 包含了 n 個節點，對節點編號做出的某一種排列
# 要滿足圖 G 的任一一個有向邊 (u, v)，u 都要排在 v 前面
# 如果 G 中存在環，那就不滿足拓樸排序的要求
# 拓樸排序的結果不只一種
# 拓樸排序的時間複雜度是 O(n+m) n 個點 m 條邊 (這其實就是 BFS 的時間複雜度)

# 複雜度分析:
# 圖的節點數為V (課程數)
# 圖的邊數為E (約束數量)
# 時間複雜度O(V + E)
#   建圖，掃描一遍所有的邊O(E)。
#   每個節點最多入隊出隊1次，複雜度O(V)。
#   鄰接表最終會被遍歷1遍，複雜度O(E)。
#   綜上，總複雜度為O(E + V)。
# 空間複雜度O(V + E)
#   鄰接表佔用O(E + V)的空間。
#   隊列最劣情況寫佔用O(V)的空間。
#   綜上，總複雜度為O(V + E)。

# 拓樸排序三步驟
# 1. 統計每個點的 indegree
# 2. 把所有 indegree = 0 的點放到 queue
# 3. 把 queue 中的點跳出來，然後對應到的鄰居點的 indegree 減一

拓扑排序三步：统计入度，零入度入队，出队并且邻居入度减一

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
 
# 方法2: 把函數包裝起來，讓主函數變得簡潔
class Solution:
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
        
    def get_indegree(self, graph):
        indegree = dict()
        for node in graph:
            indegree[node] = 0 # 先初始化每個點的 indegree 為 0
            
        for node in graph:
            for neighbor in node.neighbors:
                # node 的每個鄰居，都有一條由 node 指向它的邊
                indegree[neighbor] = indegree[neighbor] + 1
                
        return indegree
    
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

