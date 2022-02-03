class Solution:
    """
    @param a: parameter of the equation
    @param b: parameter of the equation
    @param c: parameter of the equation
    @return: a double array, contains at most two root
    """
    def rootOfEquation(self, a, b, c):
        # write your code here
        # 先判斷方程式是否有根
        if b**2 - 4*a*c < 0:
            return []
        
        # 如果方程式有根，那可能是兩個根，也可能只有一個根
        # 有兩個根的時候，輸出要排序
        root1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        root2 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        if root1 == root2:
            return [root1]

        if root1 < root2:
            return [root1, root2]
        else:
            return [root2, root1]
