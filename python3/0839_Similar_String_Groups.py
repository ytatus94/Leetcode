class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        if strs is None or len(strs) == 0:
            return 0

        # 建立鄰接表，用來表示節點之間的關係，可以構成圖
        adjacency = [[] for i in range(len(strs))]

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if self.is_similar(strs[i], strs[j]):
                    adjacency[i].append(j)
                    adjacency[j].append(i)

        # 用來判斷圖上的節點有沒有走過
        visited = [0 for i in range(len(strs))]
        count = 0
        
        for i in range(len(strs)):
            if not visited[i]:
                self.dfs(i, adjacency, visited)
                count += 1

        return count

    def is_similar(self, str1, str2):
        diff = 0 # str1 和 str2 相差多少個字元
        # 因為 str1 和 str2 是 anagram 所以長度一定相同
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1

        if diff == 0 or diff == 2:
            return True
        return False

    def dfs(self, node, adjacency, visited):
        visited[node] = True # 有走過就標記起來
        # 走 node 的鄰居
        for neighbor in adjacency[node]:
            # 如果有沒走過的鄰居，就繼續走下去
            if not visited[neighbor]:
                self.dfs(neighbor, adjacency, visited)
