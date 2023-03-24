class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def is_strobogrammatic(self, num: str) -> bool:
        # write your code here
        map_num = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in map_num.keys() or num[j] not in map_num.keys():
                return False
            elif map_num[num[i]] != num[j]:
                return False
            i += 1
            j -= 1

        return True

        
