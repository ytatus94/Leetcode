class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            idx = nums2.index(i)
            find = False
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    find = True
                    break # 離開 j 的 for 迴圈
            if not find:
                res.append(-1)
                continue
        return res
