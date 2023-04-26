class Solution:
    # 457. Classical Binary Search
    def findPosition(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2 # 整數除法
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    # 14.First Position of Target
    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    # 458. Last Position of Target (locked)
    def lastPosition(self, nums, target):
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid
            elif nums[start] <= target:
                start = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

    # 74. First Bad Version
    def findFirstBadVersion(self, n):
        start, end = 1, n

        while start + 1 < end:
            mid = start + (end - start) // 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid

        if SVNRepo.isBadVersion(start):
            return start
        else:
            return end
        return

    # 447. Search in a Big Sorted Array (locked)
    def searchBigSortedArray(self, reader, target):
        length = 1
        while reader[length - 1] < target: # 先找出包含 target 的長度
            length = length * 2

        start = 0
        end = length - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader[mid] < target:
                start = mid
            else:
                end = mid

        if reader[start] == target:
            return start
        if reader[end] == target:
            return end
        return -1

    # 159. Find Minimum in Rotated Sorted Array
    def find_min(self, nums: List[int]) -> int:
        target = nums[-1]

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid

        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]

    # 600. Smallest Rectangle Enclosing Black Pixels
    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
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
            if self.is_empty_row(image, mid):
                end = mid
            else:
                start = mid

        if self.is_empty_row(image, end):
            return start
        return end

    def find_left(self, image, y):
        start = 0
        end = y

        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_empty_col(image, mid):
                start = mid
            else:
                end = mid

        if self.is_empty_col(image, start):
            return end
        return start

    def find_right(self, image, y):
        start = y
        end = len(image[0]) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.is_empty_col(image, mid):
                end = mid
            else:
                start = mid

        if self.is_empty_col(image, end):
            return start
        return end

    def is_empty_row(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == '1':
                return False
        return True

    def is_empty_col(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return False
        return True

    # 28. Search a 2D Matrix
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        if rows == 0:
            return False
        if cols == 0:
            return False

        start = 0
        end = rows - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            elif matrix[mid][0] > target:
                end = mid

        target_row = 0
        if matrix[end][0] > target:
            target_row = start
        else:
            target_row = end

        head = 0
        tail = len(matrix[target_row]) - 1

        while head + 1 < tail:
            mid = head + (tail - head) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                head = mid
            elif matrix[target_row][mid] > target:
                tail = mid

        if (matrix[target_row][head] == target or
            matrix[target_row][tail] == target):
            return True
        return False

    # 38. Search a 2D Matrix II
    def search_matrix(self, matrix: List[List[int]], target: int) -> int:
        # write your code here
        if matrix is None or len(matrix[0]) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        count = 0
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] == target:
                count += 1
                row += 1
                col = cols - 1

        return count

    # 61. Search for a Range
    def searchRange(self, a, target):
        result = [-1, -1]
        if len(a) == 0:
            return result

        start = 0
        end = len(a) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if a[mid] < target:
                start = mid
            else:
                end = mid

        if a[start] == target:
            result[0] = start
        elif a[end] == target:
            result[0] = end
        else:
            return result

        start = result[0]
        end = len(a) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if a[mid] <= target:
                start = mid
            else:
                end = mid

        if a[end] == target:
            result[1] = end
        elif a[start] == target:
            result[1] = start

        return result

    # 462. Total Occurrence of Target (locked)
    def total_occurrence(self, a: List[int], target: int) -> int:
        if a is None or len(a) == 0:
            return 0

        count = 0
        for i in a:
            if i == target:
                count += 1

        return count

    # 585. Maximum Number in Mountain Sequence
    def mountain_sequence(self, nums: List[int]) -> int:
        # return max(nums)
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[mid + 1]:
                start = mid
            else:
                end = mid

        print(start, end)

        if nums[start] > nums[end]:
            return nums[start]
        else:
            return nums[end]

    # 75. Find Peak Element
    def find_peak(self, a: List[int]) -> int:
        start = 0
        end = len(a) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if a[mid] < a[mid + 1]:
                start = mid
            if a[mid] > a[mid + 1]:
                end = mid

        if a[start] > a[end]:
            return start
        return end

    # 62. Search in Rotated Sorted Array
    def search(self, a: List[int], target: int) -> int:
        if a is None or len(a) == 0:
            return -1

        start = 0
        end = len(a) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if a[mid] > a[0]:
                if a[mid] >= target and target >= a[start]:
                    end = mid
                else:
                    start = mid
            else:
                if a[mid] <= target and target <= a[end]:
                    start = mid
                else:
                    end = mid

        if a[start] == target:
            return start
        if a[end] == target:
            return end

        return -1

    # 39. Recover Rotated Sorted Array
    def recoverRotatedSortedArray(self, nums):
        if len(nums) == 0:
            return

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # 三步翻轉法
                self.swap(nums, 0, i + 1)
                self.swap(nums, i + 1, len(nums))
                self.swap(nums, 0, len(nums))
                break

    def swap(self, nums, start, end):
        temp = nums[start: end]
        temp = temp[:: -1]
        for i in range(len(temp)):
            nums[start + i] = temp[i]

    # 1790. Rotate String II
    def rotate_string2(self, str: str, left: int, right: int) -> str:
        length = len(str)
        double_str = str + str
        total_offset = (left - right) % length

        if total_offset == 0:
            return str

        if total_offset > 0:
            start_index = total_offset
        elif total_offset < 0:
            start_index = length - total_offset

        end_index = start_index + length

        return double_str[start_index : end_index]
