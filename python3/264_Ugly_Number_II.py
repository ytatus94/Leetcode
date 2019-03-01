class Solution:
    def nthUglyNumber(self, n: int) -> int:
        queue = []
        hash = set()
        
        queue.append(1)
        hash.add(1)
        
        for i in range(n):
            ugly_number = min(hash)
            hash.remove(ugly_number)
            queue.append(ugly_number)
            
            hash.add(ugly_number * 2)
            hash.add(ugly_number * 3)
            hash.add(ugly_number * 5)
            
        return queue[-1]

# lintcode 4
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        # O(n) scan 較快
        ugly = list()
        ugly.append(1)
        
        # 三個指標分別指向誰是最後一個乘 2 的 (p2), 最後一個乘 3 的 (p3)
        # 和最後一個乘 5 的 (p5)
        p2, p3, p5 = 0, 0, 0
        
        for i in range(1, n):
            last_number = ugly[i - 1]
            
            while ugly[p2] * 2 <= last_number:
                p2 += 1
            while ugly[p3] * 3 <= last_number:
                p3 += 1
            while ugly[p5] * 5 <= last_number:
                p5 += 1
                
            min_val = min(ugly[p2] * 2, ugly[p3] * 3)
            min_val = min(min_val, ugly[p5] * 5)
            ugly.append(min_val)
            
        return ugly[n - 1]
        
class Solution:
    def nthUglyNumber(self, n):
        # O(nlogn): heap map + heap
        priority_queue = [1]
        hash_set = set()
        
        hash_set.add(1)
        
        ugly_number = []
        for i in range(n):
            # 每次找 hash set 中最小的值
            min_val = min(hash_set)
            # set() 不支持 next 操作，所以要知道下一個最小的值，唯有把目前最小值 pop 掉
            hash_set.remove(min_val)
            ugly_number.append(min_val)
            
            # 醜數的因數是 2, 3, 5，所以把當前最小的值分別乘上 2, 3, 5 就會得到醜數
            hash_set.add(min_val * 2)
            hash_set.add(min_val * 3)
            hash_set.add(min_val * 5)
            
        return ugly_number[-1]
