class Solution:
    def searchNode(graph, values, node, target):
        queue = []
        hash = []
        
        queue.append(node)
        hash.append(node)
        
        while queue:
            head = queue.pop()
            if values[head] == target:
                return head
            for neighbor in head.neighbors:
                if neighbor not in hash:
                    queue.append(neighbor)
                    hash.append(neighbor)
        return None
