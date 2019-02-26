# lintcode 605
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.build_graph(seqs) # 這個 graph 其實就是鄰接表
        topo_order = self.topological_sorting(graph)
        return topo_order == org

    def build_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
                    
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
                
        return graph
        
    def get_indegree(self, graph):
        indegrees = {node:0 for node in graph} # 初始化成 0
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
                
        return indegrees
        
    def topological_sorting(self, graph):
        indegrees = self.get_indegree(graph)
        
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node) # 把所有入度 = 0 的放到 queue 裡面當起點
               
        topo_order = []
        while queue:
            # 利用拓樸排序有相依的順序的特性
            # 當有兩種可能性時，那就不對了
            if len(queue) > 1:
                return None
            
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                # node 被 pop 出來了，所以 node 的鄰居的 indegree 都要減一
                indegrees[neighbor] -= 1 
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 檢查看看是不是 graph 的每個點都有拿來排序
        if len(topo_order) == len(graph):
            return topo_order
            
        return None
