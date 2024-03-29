from typing import (
    List,
)

from functools import cmp_to_key

class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largest_number(self, nums: List[int]) -> str:
        # write your code here
        # 先把每個元素排序
        # a, b 組成的數有 ab 和 ba
        # 如果 ab > ba 則排序後就是 a, b
        # 如果 ab < ba 則排序後就是 b, a
        nums = sorted(nums, key=cmp_to_key(self.compare))
        # 如果 a=0, b>0 那排序完一定是 b0
        # 如果排序完是 0b 那唯一的可能是 b 也是 0
        # 表示第一個數如果是 0 那整個 nums 其實都是 0
        if nums[0] == 0:
            return '0'
        else:
            return ''.join([str(i) for i in nums])

    # 在 cmp_to_key(self.compare) 呼叫時，如果 nums =[n1, n2, n3, n4]
    # 那呼叫的順序是 compare(n2, n1), compare(n3, n2), compare(n4, n3)
    def compare(self, a, b):
        if int(str(a) + str(b)) > int(str(b) + str(a)):
            return -1 # 注意這邊要傳回 -1 而不是 1，這樣 b 才會排前面
        else:
            return 1
