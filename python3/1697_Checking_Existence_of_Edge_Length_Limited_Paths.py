class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 先把 edgeList 和 queries 依照 weighted 排序
        edgeList = sorted(edgeList, key=lambda x: x[2])
        queries = sorted(enumerate(queries), key=lambda x: x[1][2]) # x[0] 是 index, x[1] 才是原本的 queries

        edge_idx = 0
        uf = UnionFind(n)
        result = [False] * len(queries)

        for idx, (p, q, limit) in queries:
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                node1 = edgeList[edge_idx][0]
                node2 = edgeList[edge_idx][1]
                uf.union(node1, node2)
                edge_idx += 1
            
            if uf.find(p) == uf.find(q):
                result[idx] = True
                
        return result

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)] #  要包含 0 ~ n 所以上限是 n+1
        self.rank = [0] * (n + 1)

    def find(self, x):
        # 找 x 的最大的老大
        # 1. x 自己就是終極頭目
        # 2. x 的老大不是終極頭目，那就繼續找 x 的老大的老大
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 比較 x 和 y 的終極頭目看誰大
        # 小的要歸順大的
        # 一樣大的話，就選一個當終極頭目，等級記得要加一級
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        
        return False
