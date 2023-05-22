# 方法 1.
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 先把 nums 的元素放到字典裡當 key 出現的次數當做 value
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # 把字典依照 value 排序，由小到大
        sorted_d = sorted(d.items(), key=lambda kv: kv[1])

        # 選出倒數 k 個 (就是次數出現最多的 k 個)
        sorted_d = sorted_d[-k:]
        result = [k for k, v in sorted_d]
        
        return result[::-1]
      
# 方法 2.
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 這是一開始自己寫的，只 beat 7.63%，太慢了
        # 先把 nums 的元素放到字典裡當 key 出現的次數當做 value
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # 把字典依照 value 排序，預設是由小到大排序，所以加上 reverse=True 由大到小排
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

        # 選出前 k 個 (就是次數出現最多的 k 個)
        result = [key for key, val in sorted_d[:k]]
        
        return result
      
# 方法 3.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1

        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = [i[0] for i in sorted_count]

        return result[:k]
