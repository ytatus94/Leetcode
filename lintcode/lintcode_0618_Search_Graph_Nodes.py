class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    
    def searchNode(self, graph, values, node, target):
        # if values[node] == target:
        #     return node

        queue = [node]
        hash_set = [node]

        while queue:
            head = queue.pop(0)
            if value[head] == target: # 找到了
                return head
            for n in head.neighbors:
                if n not in hash_set: # 判斷 n 是否出現過
                    queue.append(n)
                    hash_set(n)

        return None
