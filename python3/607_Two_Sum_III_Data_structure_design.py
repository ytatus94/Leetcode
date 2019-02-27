class TwoSum:
    nums = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.nums.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        hash_map = {}
        for idx, val in enumerate(self.nums):
            if value - val in hash_map:
                return True
            else:
                hash_map[val] = idx
        return False
