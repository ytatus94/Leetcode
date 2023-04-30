class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 分開成 alice 和 bob 兩個圖來看
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)

        edge_alice = 0
        edge_bob = 0
        total_edges = 0

        # 路徑 3 要先看，所以路徑 3 要先排在最前面
        edges = sorted(edges, key=lambda x: x[0], reverse=True)

        for edge in edges:
            # 先看 alice 和 bob 都能走的路徑 3
            if edge[0] == 3:
                if uf_alice.union(edge[1], edge[2]):
                    # 因為 alice 和 bob 都能走這個路徑 3
                    # 如果 alice 判斷須要合併 edge[1] 和 edge[2] 那 bob 也須要合併
                    uf_bob.union(edge[1], edge[2])
                    edge_alice += 1
                    edge_bob += 1
                    total_edges += 1
            elif edge[0] == 1: # 只看 alice 能走的路徑 1
                if uf_alice.union(edge[1], edge[2]):
                    edge_alice += 1
                    total_edges += 1
            elif edge[0] == 2: # 只看 bob 能走的路徑 2
                if uf_bob.union(edge[1], edge[2]):
                    edge_bob += 1
                    total_edges += 1

        # 要互相連通 --> n 個點 n-1 條邊
        if edge_alice == n - 1 and edge_bob == n - 1:
            return len(edges) - total_edges
        return -1

class UnionFind:
    def __init__(self, n):
        # 0~n 全都要放進去，所以上限是 n+1
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        # 找 x 所屬的陣營的大頭目
        # 如果 x 不是最大的大頭目，就找 x 的老大的老大
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 先找出各自陣營的老大
        root_x = self.find(x)
        root_y = self.find(y)

        # 老大不是同一個時，要合併在一起，就是大的併小的
        # 如果 root_x 比 root_y 大，那 root_x 就是 root_y 的老大
        # 如果 root_x 比 root_y 小，那 root_y 就是 root_x 的老大
        # 如果 root_x 和 root_y 一樣大，那就選一個當老大，並且把層級提高一級
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x 
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] =root_y
            else:
                self.parent[root_y] = root_x # 選了 root_x 當新的老大
                self.rank[root_x] += 1 # 所以 root_x 的層級要提高一級
            return True # x 和 y 老大不同才要合併
        
        return False # x 好 y 的老大相同，就不用合併
