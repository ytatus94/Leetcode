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
