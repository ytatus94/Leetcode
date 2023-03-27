# Course Schedule I 和 Course Schedule II 的唯一差別是
# I 只要知道能不能修完課，II 除了要能修完課還要知道修課順序
# I 不需要 hash map 和 queue 連動，只要一個計數器紀錄修了多少課
# II 需要 hash map 和 queue 連動，hash_map 中紀錄修課順序
# 基本上 I 和 II 答案一模一樣，只差在有沒有 hash map

from typing import (
    List,
)

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        # write your code here
        if prerequisites is None or len(prerequisites) == 0:
            return [i for i in range(num_courses)] # 沒有 prerequisites 時，一定能修完課

        graph = [[] for i in range(num_courses)]
        indegree = [0] * num_courses
        # 因為課程是從 0 到 n-1 剛好是數字，所以可以用 list 不必用 dict
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in) # 建立圖
            indegree[node_in] += 1 # 統計所有點的 indegree

        queue = [i for i in range(num_courses) if indegree[i] == 0] # 把所有 indegree = 0 的點放到 queue 裡面
        hash_set = [i for i in range(num_courses) if indegree[i] == 0] # 要用 hash map 記錄完成的課程順序
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    hash_set.append(neighbor)

        if len(hash_set) == num_courses: # 表示能修完課
            return hash_set # 傳回修課的順序

        return [] # 無法修完克，就沒有修課的順序了
