# 課程相依性，就需要用到 topological sorting
# 重要的是要建立課程之間關係圖，再從圖中得到 indegree
# graph[先修課程] = [修完先修課程後，可以修的其他課程]
# indegree[某課程] = 有幾個先修課程要先上

# 拓樸排序三步驟
# 1. 統計所有點的 indegree
# 2. 把 indegree=0 的點放到 queue 裡面
# 3. 從 queue 中把點跳出來，然後鄰居點的 indegree 減一


# 方法1:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: # 沒有先修課程的要求，當然能上完所有課程
            return True
        
        # 初始化 graph
        graph = {}
        for node in range(numCourses):
            graph[node] = set() # 不可以重複，所以用 set()
        # 建立圖
        for pre in prerequisites:
            graph[pre[1]].add(pre[0]) # pre[1] 是先修課，上完了才能上 pre[0]
            
        # 初始化 indegree
        indegree = {}
        for node in graph:
            indegree[node] = 0
        # 賦值
        for node in graph:
            for neighbor in graph[node]: # neighbor 就是後修課程
                indegree[neighbor] += 1 # 每個後修課程都有 node 這一個先修課程，所以要加一
                
        # topological sorting
        # 用 BFS
        queue = []
        # 把所有 indegree = 0 的 node 放到 queue 裡面
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)
                
        count = 0
        while queue:
            node = queue.pop(0) # node 表示已經上完的課程
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1 # 上完 node 了，所有以 node 為先修課程的課通通要減一
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 全部都跑完之後，若課程之間有環狀依賴，那 indegree 就不會是 0
        # 唯有全部的 indegree 都是 0 的時候才有可能會把全部的課都修完
        for k, v in indegree.items():
            if v > 0:
                return False
        return True
    
    
        # 這一題雖然是圖，但是不需要一個和 queue 連動的 hash_map，因為若使用 len(hash_map) == numCourses 是不對的
        # 可能有十幾個課程，但是只有兩三個課程有先修課程的要求，這樣子課是修得完，但是 len(hash_map) < numCourses
    
# 方法2:
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

 # lintcode 615
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        if prerequisites is None or len(prerequisites) == 0:
            return True
            
        graph = self.build_graph(prerequisites)
        return self.topo_sort(graph)
        
    def build_graph(self, prerequisites):
        graph = {}
        for pre in prerequisites:
            for course in pre:
                if course not in graph:
                    graph[course] = set()
                    
        for pre in prerequisites:
            for i in range(1, len(pre)):
                graph[pre[i]].add(pre[i - 1])
                
        return graph
    
    def get_indegree(self, graph):
        indegrees = {node:0 for node in graph} # 初始化成 0
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
                
        return indegrees
        
    def topo_sort(self, graph):
        indegrees = self.get_indegree(graph)
        
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        
        while queue:
            course = queue.pop(0)
            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        for k, v in indegrees.items():
            if indegrees[k] != 0:
                return False
        return True
