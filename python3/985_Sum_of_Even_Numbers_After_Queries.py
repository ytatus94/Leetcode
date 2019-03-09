class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        # 先把原本 A 中所有的偶數加起來
        even_sum = sum([num for num in A if num % 2 == 0])

        # 檢查 A[index] + val 後是奇數還是偶數
        # A[index] + val 是偶數的時候有兩種可能
        # A[index] 和 val 都是奇數: 直接把 A[index] + val 加入 even_sum
        # A[index] 和 val 都是偶數: 只要把 val 加入 even_sum (因為 A[index] 已經被加入了)
        # A[index] + val 是奇數時
        # 如果是 A[index] (偶) 配上 val (奇)，那要把 A[index] 從 even_sum 中扣除掉
        # 如果是 A[index] (奇) 配上 val (偶)，那什麼都不做
        res = []
        for val, index in queries:
            if A[index] % 2 == 0 and val % 2 == 0:
                even_sum += val
            elif A[index] % 2 != 0 and val % 2 != 0:
                even_sum += A[index] + val
            elif A[index] % 2 == 0 and val % 2 != 0:
                even_sum -= A[index]
                
            # 然後要記得把 A[index] 更新為 A[index] + val
            A[index] += val

            res.append(even_sum)
        
        return res

# 會超時
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(queries)):
            index = queries[i][1]
            A[index] += queries[i][0]
            res.append(sum([j for j in A if j % 2 == 0]))
        return res
