class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        # 看到別人寫的方法，比較短又快
        # 預設每個元素對應到課程 0 ~ numCourses
        # graph 中紀錄的是先修課程 (用元素的位置來代表) 對應到的可修課程 (該元素位置的值)
        # indegree 也是用值來代表該元素對應的入度
        graph = [[] for _ in range(numCourses)] # 初始化都是空的
        indegrees = [0 for _ in range(numCourses)] # 初始化為 0
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
        
        can_finish = 0
        
        q = collections.deque()
        
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)
        
        while q:
            finished = q.popleft()
            can_finish += 1
            for course in graph[finished]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)
        
        return can_finish == numCourses
        
#         if len(prerequisites) == 0:
#             return True
        
#         # 初始化 graph
#         graph = {}
#         for pre in prerequisites:
#             for node in pre:
#                 graph[node] = set()
#         # 建立圖  
#         for pre in prerequisites:
#             graph[pre[1]].add(pre[0])
            
#         # 初始化 indegree
#         indegree = {}
#         for node in graph:
#             indegree[node] = 0
#         # 賦值
#         for node in graph:
#             for neighbor in graph[node]:
#                 indegree[neighbor] += 1
                
#         # topological sorting
#         # 用 BFS
#         queue = []
#         # 把所有 indegree = 0 的 node 放到 queue 裡面
#         for node in graph:
#             if indegree[node] == 0:
#                 queue.append(node)
                
#         count = 0
#         while queue:
#             node = queue.pop(0)
#             count += 1
#             for neighbor in graph[node]:
#                 indegree[neighbor] -= 1
#                 if indegree[neighbor] == 0:
#                     queue.append(neighbor)
                    
#         # 全部都跑完之後，若課程之間有環狀依賴，那 indegree 就不會是 0
#         # 唯有全部的 indegree 都是 0 的時候才有可能會把全部的課都修完
#         for k, v in indegree.items():
#             if v > 0:
#                 return False
#         return True
