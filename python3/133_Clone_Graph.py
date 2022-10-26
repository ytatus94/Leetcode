# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # clone graph 的三個步驟
        # 1. 用 BFS 找到所有的點
        # 2. 拷貝所有的點
        # 3. 拷貝所有的邊
        
        if node is None:
            return node
        
        # 1. 用 BFS 找到所有的點
        nodes = self.get_nodes(node)
        
        # 2. 拷貝所有的點
        mapping = {} # dictionary 就是 hash map
        # 不可以用 for node in nodes
        # 因為 python 的 scope 造成 for 的 node 再迴圈之外一樣是可見的
        # 會修改到原本輸入的 node
        for n in nodes:
            # 拷貝 node 的值，等號左邊是新的點，右邊是對應到的值 (由舊的點得到)
            # 因為 UndirectedGraphNode 有點的值和鄰居兩個資料成員
            # 這邊只是先指定點的值，鄰居還是空的
            mapping[n] = UndirectedGraphNode(n.label)
            
        # 3. 拷貝所有的邊
        for n in nodes:
            new_node = mapping[n]
            for neighbor in n.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
                
        return mapping[node] # 傳回拷貝過後的，以 node (這是在新的圖上的 node) 為起點的圖
        
    def get_nodes(self, node):
        # BFS 的三步驟
        # 1. 把所有起點放到 queue
        # 2. 用 while loop 不斷的從 queue 中 pop 出來
        # 3. 把下一層放到 queue 中
        
        queue = []
        result = [] # 圖的時候，要用一個 has map 來記錄有沒有走過該點
        
        # 1. 把所有的起點放到 queue
        queue.append(node)
        result.append(node) # 和 queue 同步 (對 hash map 要做一樣的動作)
        
        # 2. 用 while loop 不斷的從 queue 中 pop 出來
        while queue:
            head = queue.pop(0)
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.append(neighbor)
                    queue.append(neighbor)
                    
        return result

# lintcode 137
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return
        
        # 用 BFS 找到所有的點
        nodes = self.get_all_nodes(node)
        # clone 所有的點
        mapping = dict()
        for n in nodes:
            mapping[n] = UndirectedGraphNode(n.label)
            
        # clone 所有的邊
        for n in nodes:
            new_node = mapping[n]
            for neighbor in n.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
                
        return mapping[node]
        
    def get_all_nodes(self, node):
        if node is None:
            return []
            
        q = [node]
        hash = [node]
        
        while q:
            n = q.pop(0)
            for neighbor in n.neighbors:
                if neighbor not in hash:
                    q.append(neighbor)
                    hash.append(neighbor)
        
        return hash
