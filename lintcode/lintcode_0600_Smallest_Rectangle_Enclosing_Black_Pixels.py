from typing import (
    List,
)

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
        # write your code here
        # 仔細看範例的話可以知道 x 其實是 rows 而 y 是 columns
        self.n_rows = len(image)
        self.n_cols = len(image[0])

        top = self.find_top(image, x)
        bottom = self.find_bottom(image, x)
        left = self.find_left(image, y)
        right = self.find_right(image, y)

        return (bottom - top + 1) * (right - left + 1)
    
    # 找第一個不是全為 0 的 row
    def find_top(self, image, row):
        start = 0
        end = row
        while start + 1 < end:
            mid = start + (end - start) // 2
            if "1" in image[mid]:
                end = mid
            else:
                start = mid
        if "1" in image[start]:
            return start
        else:
            return end

    # 找最後一個不是全為 0 的 row
    def find_bottom(self, image, row):
        start = row
        end = self.n_rows - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if "1" in image[mid]:
                start = mid
            else:
                end = mid
        if "1" in image[end]:
            return end
        else:
            return start

    # 找第一個不是全為 0 的 column
    def find_left(self, image, column):
        start = 0
        end = column
        while start + 1 < end:
            mid = start + (end - start) // 2
            # 要看在 mid 這個 column 上的所有 row 有沒有 1
            if self.is_empty_column(image, mid):
                start = mid
            else:
                end = mid
        if self.is_empty_column(image, start):
            return end
        else:
            return start

    # 找最後一個不是全為 0 的 column
    def find_right(self, image, column):
        start = column
        end = self.n_cols - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_empty_column(image, mid):
                end = mid
            else:
                start = mid
        if self.is_empty_column(image, end):
            return start
        else:
            return end
    
    # 判斷是不是 empty column
    def is_empty_column(self, image, column):
        # 要看這個 column 上的所有 row 的元素
        # 只要有元素是 1 就不是 empty column
        for row in range(self.n_rows):
            if image[row][column] == "1":
                return False
        return True
