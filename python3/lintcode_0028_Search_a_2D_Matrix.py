from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        # write your code here
        start_row = 0
        end_row = len(matrix) - 1

        while start_row + 1 < end_row:
            mid_row = start_row + (end_row - start_row) // 2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] < target:
                start_row = mid_row
            elif matrix[mid_row][0] > target:
                end_row = mid_row
        
        if matrix[start_row][0] <= target < matrix[end_row][0]:
            return self.search_in_raw(matrix[start_row], target)
        elif matrix[end_row][0] <= target:
            return self.search_in_raw(matrix[end_row], target)
        return False


    def search_in_raw(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False
