class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for k, v in hash.items():
            if v == 1:
                return k
        
        '''
        用數學來找
        nums = [a,a,b,b,c], set(nums)=[a,b,c]
        2*(a+b+c) - (a+a+b+b+c) = 2c-c = c
        '''
        return sum(set(nums))*2-sum(nums)
