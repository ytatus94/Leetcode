# lintcode 178
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        # 要是樹的條件是 n 個點有 n-1 條邊 n 個點要互相連通
        if n == 0:
            return False

        if len(edges) != n - 1:
            return False
    
        # 特別的情形
        # 當 n=1 且 edge 是空的時候，for u, v in edges 不會執行
        # 所以 neighbors 會變空
        if n == 1 and len(edges) == 0:
            return True
    
        # 給定編號從 0 ~ n-1 的 n 個點
        # 所以就從 0 出發看看能不能訪問到其他所有的點
        
        # 先建立鄰接表
        neighbors = dict()
        for u, v in edges:
            if u not in neighbors:
                neighbors[u] = [v]
            else:
                neighbors[u].append(v)
                
            if v not in neighbors:
                neighbors[v] = [u]
            else:
                neighbors[v].append(u)
        
        # 標準的 BFS
        queue = [0]
        hash_map = [0] # 用 hash map 來記錄有沒有走過該點，要和 queue 同步處理
        
        while queue:
            node = queue.pop(0)
            for i in neighbors[node]:
                if i in hash_map:
                    continue
                queue.append(i)
                hash_map.append(i)
                
        return len(hash_map) == n
