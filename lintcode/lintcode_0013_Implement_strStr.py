# 方法1
# index() 傳回 index，如果找不到就會有 ValueError
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        if target in source:
            return source.index(target)
        else:
            return -1

# 方法2
# find() 傳回 index，如果找不到就會傳回 -1
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        return source.find(target)

# 方法3
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        for i in range(len(source)-len(target) + 1):
            if source[i: i+len(target)] == target:
                return i
        return -1
