from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        # 圖如果是樹：會有 n 個點，n-1 條邊，n 個點互相連通
        # 各種樹都可以，不一定要是 binary tree
        if n != len(edges) + 1:
            return False

        # 建立鄰接表，紀錄 node 和它的鄰居
        # n1 和 n2 是鄰居，就要記錄 n1 的鄰居是 n2，也要記錄 n2 的鄰居是 n1
        adjacency = {}
        for n1, n2 in edges:
            if n1 in adjacency.keys():
                adjacency[n1].append(n2)
            else:
                adjacency[n1] = [n2]

            if n2 in adjacency.keys():
                adjacency[n2].append(n1)
            else:
                adjacency[n2] = [n1]
        print(adjacency)

        # 用 BFS 去走每個點，走過就紀錄下來
        queue = [0]
        hash_set = [0]
        while queue:
            node = queue.pop(0)
            if node in adjacency.keys():
                for next_node in adjacency[node]:
                    # 如果 next_node 在 hash_set 裡面了，表示已經走過了，
                    # 不可以往回頭走，不然會變成無限迴圈
                    # 0--1--2 如果從 0 出發走到 1，1 的下一層有 0 和 2
                    # 這時候不能往回走到 0，不然就變鬼打牆
                    if next_node in hash_set:
                        continue
                    queue.append(next_node)
                    hash_set.append(next_node)

        return len(hash_set) == n
