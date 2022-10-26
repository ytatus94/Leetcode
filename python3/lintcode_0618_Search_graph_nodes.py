# 題目:
# 給定一張無向圖，一個節點以及一個目標值，返回距離這個節點最近 且 值為目標值的節點，如果不能找到則返回 NULL。
# 在給出的參數中, 我們用 map 來存節點的值

class Solution:
    def searchNode(self, graph, values, node, target):
        queue = []
        hash = []
        
        queue.append(node)
        hash.append(node)
        
        while queue:
            head = queue.pop()
            if values[head] == target: # values 是一個紀錄節點的值的 dict
                return head
            for neighbor in head.neighbors:
                if neighbor not in hash: # 鄰居不在 hash 裡面，就表示還沒有走過
                    queue.append(neighbor)
                    hash.append(neighbor)
        return None
