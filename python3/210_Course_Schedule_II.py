class Solution:
    def findOrder(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        graph = self.build_graph(numCourses, prerequisites)
        indegrees = self.get_indegrees(numCourses, prerequisites)
        topo_order = self.topological_sort(graph, indegrees)
        return topo_order
        
    def build_graph(self, numCourses, prerequisites):
        graph = {i: set() for i in range(numCourses)}
        
        for course, pre in prerequisites:
            graph[pre].add(course)
        
        return graph

    def get_indegrees(self, numCourses, prerequisites):
        indegrees = {i: 0 for i in range(numCourses)}
        
        for course, pre in prerequisites:
            indegrees[course] += 1
        
        return indegrees
        
    def topological_sort(self, graph, indegrees):
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
                
        topo_order = []
        while queue:
            node = queue.pop(0)
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    

        if len(topo_order) == len(graph):
            return topo_order
        return []

# lintcode 616
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        graph = [[] for i in range(numCourses)]
        indegrees = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
        
        queue = []
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
                
        topo_order = []
        while queue:
            course = queue.pop(0)
            topo_order.append(course)
            for i in graph[course]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
                    
        return topo_order if len(topo_order) == numCourses else []
