# lintcode 139
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
            
        # 先計算 prefix sum
        pre_sum = [(0, -1)]
        for idx, val in enumerate(nums):
            sum = pre_sum[-1][0] + val
            pre_sum.append((sum, idx))
            
        # 計算兩兩前綴和的差
        # sum(i~j) = PrefixSum[j+1] - PrefixSum[i]
        # 照題目的要求，這個差要盡量接近於 0
        # 要盡量接近於 0 的話，可以對前綴和數組排序
        # 計算相鄰的兩個前綴和的值
        
        # 排序前綴和數組
        pre_sum = sorted(pre_sum)
        
        closet = sys.maxsize # 這個要越接近 0 越好，所以先設成一個很大的數
        result = []
        for i in range(1, len(pre_sum)):
            pre_sum_diff = pre_sum[i][0] - pre_sum[i - 1][0]
            if closet > pre_sum_diff:
                closet = pre_sum_diff
                # 找到一組較小的前綴和差
                # 所以要取得在原始數組 (非前綴和數組) 中正確的 index
                # start index 是兩者較小的那個 index + 1
                # 加 1 是因為第 m ~ 第 n 個數的和是前 n 個數的前綴和減去前 m-1 個數的前綴和
                # 是 m 與 m-1 的關係
                start_index = min(pre_sum[i - 1][1], pre_sum[i][1]) + 1
                end_index = max(pre_sum[i - 1][1], pre_sum[i][1])
                print(start_index, end_index)
                result = [start_index, end_index]
        
        return result
