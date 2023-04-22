class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        # 把 nums[i] 某部分的數值，搬到 nums[i - 1]
        # 這樣一直搬的話， nums[0] 的數值會越來越大，要找出一個最小的 nums[0]
        # 所以答案一定是介於 nums[0] 和 max(nums) 之間的某個數 k
        # 用二分法找出這個 k 值

        start = nums[0]
        end = max(nums)

        while start < end: # 這邊不能寫 start + 1 < end 這樣離開回圈時 start = end
            mid = start + (end - start) // 2 # 就是某個數 k
            space = 0 # nums[i] 和 k 之間有多少空間，可以容納來自後面搬過來的數值
            flag = True # 判斷空間夠不夠
            for i in range(len(nums)):
                if nums[i] < mid: # 有空間 mid - nums[i] 可以容納來自後面的數值
                    space += mid - nums[i]
                else:
                    space -= nums[i] - mid # nums[i] 比 mid 大的時候，會把數值往前面搬，因此佔用了可用空間

                if space < 0: # 可用空間都被用光了，所以無法再搬動
                    flag = False
                    break

            if flag: # 目前找到的 mid 是 nums[0] 最大值的其中一個可能值，但是可能會有更小的值，答案一定在 start ~ mid 之間
                end = mid
            else: # 目前找到的 mid 沒辦法使 nums[0] 容納後面搬過來的數，所以答案一定在 mid ~ end 之間
                start = mid + 1

        # 離開迴圈時就是找到了，此時 start = end 就是答案

        return end
