class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # 先判斷要 reshape 的維度和原本的維度
        # 如果維度不同，就傳回原本的矩陣
        if r * c > len(nums) * len(nums[0]):
            return nums
        
        # 把 nums 扁平化，然後再按照順序塞到新的 matrix 上
        flatten = [x for row in nums for x in row]
        
        reshaped = []
        k = 0 # 用來 loop flatten 的元素
        for i in range(r):
            row = [0] * c # 先建立 c 個元素都是 0 的列
            for j in range(c):
                row[j] = flatten[k]
                k += 1
            reshaped.append(row)

        return reshaped
