# 方法1:
from typing import (
    List,
)

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        if prerequisites is None or len(prerequisites) == 0:
            return True
        
        # 找出所有課程 (不可以重複)
        all_courses = set()
        for pair in prerequisites:
            for i in pair:
                all_courses.add(i)

        # 先建立一個課程間的關係的 graph
        # key 是先修課程 value 是後修課程的 list，要 key-value 的注意順序
        graph = {}
        for i in all_courses:
            graph[i] = [] # 這只是 placeholder
        for pair in prerequisites:
            # pair[0]: 後修課程
            # pair[1]: 先修課程
            graph[pair[1]].append(pair[0])
        # graph={先修課程: [修完可以修這些課]}

        # 找出每個課程的 indegree
        indegree = {}
        for i in all_courses:
            indegree[i] = 0 # 這也是 placeholder
        for k in graph.keys():
            for c in graph[k]: # c 是需要先修 k 才能修的課程
                indegree[c] += 1
        # indegree={課程: 有幾門先修課}

        start_courses = [k for k, v in indegree.items() if v == 0]
        # 如果沒有課程的 indegree 是 0 就表示沒辦法滿足修課的要求
        if len(start_courses) == 0:
            return False

        queue = [c for c in start_courses]
        hash_set = [c for c in start_courses] # 保存 indegree = 0 的課程 (就是上完的課程)

        while queue:
            finished_course = queue.pop(0)
            for next_course in graph[finished_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    hash_set.append(next_course)

        for k, v in indegree.items():
            if v != 0:
                return False

        return True

# 方法2:
from typing import (
    List,
)

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        if prerequisites is None or len(prerequisites) == 0:
            return True

        # 建立 graph
        # node out ----> node in 箭頭由 out 指向 in
        graph = {x: [] for x in range(num_courses)} # 空的
        for pair in prerequisites:
            course = pair[0] # node in
            pre_course = pair[1] # node out
            graph[pre_course].append(course) # 賦值

        # 拓樸排序三步驟
        # 1. 統計所有點的 indegree
        # 2. 把所有 indegree = 0 的點放到 queue 裡面
        # 3. 把 queue 中的點跳出來，對應到的鄰居點的 indegree 減一
        indegree = {x: 0 for x in range(num_courses)}
        for pair in prerequisites:
            course = pair[0] # node in
            # pre_course = pair[1] # node out
            indegree[course] += 1

        queue = [i for i in range(num_courses) if indegree[i] == 0]
        hash_set = [i for i in range(num_courses) if indegree[i] == 0]
        while queue:
            finished = queue.pop(0)
            for c in graph[finished]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
                    hash_set.append(c)

        return len(hash_set) == num_courses
      
# 方法3: 因為方法 2 中建立圖和統計 indegree 時都要 loop prerequisites 所以可以合併在一起做
from typing import (
    List,
)

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        graph = {i: [] for i in range(num_courses)} # 建立圖
        indegree = {i: 0 for i in range(num_courses)} # 統計所有點的 indegree
        for course, pre_course in prerequisites:
            graph[pre_course].append(course) # 賦值
            indegree[course] += 1 # 賦值

        # 把所有 indegree=0 的點放到 queue 裡面
        queue = [i for i in range(num_courses) if indegree[i] == 0]
        num_of_finished_course = 0 # 只需要知道修完的課的數量，不需要知道哪些課修完了，所以不用 hash map
        # 不斷地把 queue 的點跳出來，對應的鄰居點的 indegree 減一
        while queue:
            finished_course = queue.pop(0)
            num_of_finished_course += 1
            for next_course in graph[finished_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return num_of_finished_course == num_courses
