# 方法 1.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 統計每一個點的出度和入度
        # 指向該點就加一，該點指出去就減一
        arr = [0 for _ in range(n + 1)]
        for t in trust:
            arr[t[0]] -= 1
            arr[t[1]] += 1

        for i in range(1, len(arr)):
            if arr[i] == n - 1: # 入度 = n-1 且出度 = 0 的時候就是答案
                return i

        return -1
      
# 方法 2.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 統計每個點的出度和入度
        # 出度 = 0 且入度 = n-1 的點就是答案
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for t in trust:
            indegree[t[1]] += 1
            outdegree[t[0]] += 1

        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        
        return -1
