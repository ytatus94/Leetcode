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
