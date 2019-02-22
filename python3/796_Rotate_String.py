class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # 如果 B 是 A 的 rotate string
        # 那 B 一定會在 A + A 裡面
        # 例如 ab(cdeab)cde
        return B in A + A and len(B) == len(A)

# lintcode 8
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if offset > len(str) and len(str) > 0:
            offset = offset % len(str)
            
        # abcdefgabcdefg
        temp = (str * 2)[len(str) - offset : 2 * len(str) - offset]
        
        for idx in range(len(str)):
            str[idx] = temp[idx] # 要修改原本的 str
