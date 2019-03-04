class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        nums = sorted(A)
        
        # 找第一個正數的索引
        i = 0
        j = 0
        while j < len(nums) and nums[j] < 0:
            j += 1
        # 離開迴圈時 j 停在第一個正數上面
        
        # 看正數還是負數哪個比較多，多的要開頭，一樣多的時候誰開頭都可以
        # 第一個正數 j 的前面都是負數，因為從 0 算起，所以負數的數目就是 j 個
        # 正數的數目是 len - j
        if j < len(nums) - j: # 正數多，所以正數開頭
            nums = nums[j:] + nums[:j] # 把正負數的順序顛倒
            i = 0
            j = len(nums) - j
            # j 現在變成第一個負數的索引，因為有 len - j 個正數，又索引從 0 開始
            # 所以 j 就變成 len - j
            
        while i < j and j < len(nums):
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 2
            j += 1
            
        for i in range(len(A)):
            A[i] = nums[i]
