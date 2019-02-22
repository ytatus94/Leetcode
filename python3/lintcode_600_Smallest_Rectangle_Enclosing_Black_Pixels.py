class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        top = self.find_top(image, x)
        bottom = self.find_bottom(image, x)
        left = self.find_left(image, y)
        right = self.find_right(image, y)
        return (bottom - top + 1) * (right - left + 1)

    def find_top(self, image, x):
        start = 0
        end = x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_empty_row(image, mid):
                start = mid
            else:
                end = mid
        if self.is_empty_row(image, start):
            return end
        return start

    def find_bottom(self, image, x):
        start = x
        end = len(image) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            print(start, end, mid)
            if self.is_empty_row(image, mid):
                end = mid
            else:
                start = mid
        if self.is_empty_row(image, end):
            return start
        else:
            return end
    
    def find_left(self, image, y):
        start = 0
        end = y
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_empyt_col(image, mid):
                start = mid
            else:
                end = mid
        if self.is_empyt_col(image, start):
            return end
        else:
            return start
    
    def find_right(self, image, y):
        start = y
        end = len(image[0]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_empyt_col(image, mid):
                end = mid
            else:
                start = mid
        if self.is_empyt_col(image, end):
            return start
        else:
            return end
    
    def is_empty_row(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == '1':
                return False
        return True
        
    def is_empyt_col(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return False
        return True
