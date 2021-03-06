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
        # 找起點
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

# lintcode 120
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if end not in dict:
            dict.add(end)
            
        queue = [(start, 1)]
        
        while queue:
            word, dist = queue.pop(0)
            if word == end:
                return dist
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == ch:
                        continue
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in dict:
                        queue.append((new_word, dist+1))
                        dict.remove(new_word)
        
        return 0
        
class Solution:
    def ladderLength(self, start, end, dict):
        if len(dict) == 0:
            return 0
        
        if start == end:
            return 1
        
        if end not in dict:
            dict.add(end) # dict 是一個 set() 所以用 add()
        
        queue = [start]
        hash_set = set([start]) # 不知道為什麼要用 set() 才不會超時
        length = 0
        
        while queue:
            length += 1
            for i in range(len(queue)): # 層級遍歷
                word = queue.pop(0)
                if word == end:
                    return length
                for new_word in self.get_next_word(word, dict):
                    if new_word in hash_set: # 已經用過的單字不可再使用
                        continue
                    queue.append(new_word)
                    hash_set.add(new_word)
        return 0
        
    def get_next_word(self, word, dict):
        new_words = []
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == ch:
                    continue
                new_word = word[:i] + ch + word[i+1:]
                if new_word in dict:
                    new_words.append(new_word)
        return new_words
