class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            if i % 2 != 0:
                continue
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        if len(hash_map) == 0:
            return -1
        else:
            largest_count = 0
            curr_key = None
            for k, v in hash_map.items():
                if v > largest_count:
                    largest_count = v
                    curr_key = k
                elif v == largest_count:
                    if k < curr_key:
                        curr_key = k

            return curr_key
