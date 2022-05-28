class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def rotate_string2(self, str: str, left: int, right: int) -> str:
        # write your code here
        length = len(str)
        # 這種 rotate string 的題目常常需要把原先的 string 變成原來的兩倍
        # abcdefg --> (abcdefg)(abcdefg)
        double_str = str + str
        # 有時候 left 和 right offset 的長度會比 string 的長度還長，要先求餘數
        total_offset = (left - right) % length

        print(left, right, total_offset)

        if total_offset == 0:
            return str

        result = None
        if total_offset > 0:
            # 如果 total_offset 是正數，就是表示原先的 string 向右移動
            # --> 用第一部分的 (abcdefg) 來選取 start index = total_offset, 長度是 length 的字串
            start_index = total_offset
        elif total_offset < 0:
            # 如果是負數，就是原先的 string 向左移動
            # --> 用第二部分的 (abcdefg) 來選許，此時的 a 的 index 是 length
            # 所以 start index = length - total_offset, 一樣長度選取的是 length
            start_index = length - total_offset
        end_index = start_index + length
        results = double_str[start_index: end_index]
        return results



