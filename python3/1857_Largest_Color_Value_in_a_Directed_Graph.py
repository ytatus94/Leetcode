class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors) # node 的數目
        m = len(edges)

        # 要利用路徑上前面一個 node 的每個顏色最大頻率，再加上當前 node 的顏色
        # 來得知當前 node 上每個顏色的最大頻率
        # 前一個 node 一定要先求，所以是拓樸排序

        # topo 排序:
        # 1. 建立圖, 2. 統計入度, 3. 入度=0 的放入 queue,
        # 4. 從 queue pop 出來，並且鄰居的入度減一 (bfs)
        graph = {}
        indegree = {}
        for i in range(n):
            graph[i] = set()
            indegree[i] = 0

        for edge in edges:
            graph[edge[0]].add(edge[1])
            indegree[edge[1]] += 1

        # 每一個 node 可能有很多入度 (能達到 node 的不同路徑)
        # 所以每個顏色都有可能，要開一個 n row 26 col 的陣列來
        # 記錄每個 node 的每種顏色的最大頻率
        count = [[0 for j in range(26)] for i in range(n)]
        visited = 0 # 用來計算走過幾個 node 了
        result = 0

        queue = [k for k, v in indegree.items() if v == 0]

        while queue:
            node = queue.pop(0)
            curr_color = colors[node] # 這是 str 要把它轉換成 index 才能用在 count
            count[node][ord(curr_color) - ord('a')] += 1
            # 可能有好幾條路徑可以走到 node 所以要從這些路徑裡面找出最大值
            result = max(result, count[node][ord(curr_color) - ord('a')])
            visited += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

                # 更新鄰居的顏色
                # 還沒有走到鄰居，所以鄰居的每種顏色的最大可能頻率會和當前的點一樣
                # 或是更大 (可能鄰居有別的路徑可以到達，造成頻率更大)
                for i in range(26):
                    count[neighbor][i] = max(count[neighbor][i], count[node][i])
       
        # 當走過的點數和全部的 node 數目一樣的時候，才沒有環
        if visited == n:
            return result
        return -1
        
        
