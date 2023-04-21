class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # 9. Fizz Buzz
    def fizzBuzz(self, n):
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('fizz buzz')
            elif i % 3 == 0:
                result.append('fizz')
            elif i % 5 == 0:
                result.append('buzz')
            else:
                result.append(str(i))

        return result

    # 37. Reverse 3-digit Integer
    def reverse_integer(self, number: int) -> int:
        c = number % 10
        b = (number // 10) % 10
        a = (number // 100) % 10

        return c * 100 + b * 10 + a

    # 239. Root of Equation (locked)
    def rootOfEquation(self, a, b, c):
        if b**2 - 4*a*c < 0:
            return []

        root1 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
        root2 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)

        if root1 == root2:
            return [root1]

        if root1 < root2:
            return [root1, root2]
        else:
            return [root2, root1]

    # 241. String To Integer (locked)
    def stringToInteger(self, target):
        return int(target)

    # 8. Rotate Character Array
    def rotate_string(self, s: List[str], offset: int):
        if s is None or len(s) == 0:
            return
        
        double_str = s + s
        offset = offset % len(s)

        start_index = len(s) - offset
        end_index = start_index + len(s)

        new_string = double_str[start_index : end_index]

        for i in range(len(s)):
            s[i] = new_string[i]

    # 172. Remove Element
    def removeElement(self, A, elem):
        result = []

        for i in A:
            if i != elem:
                result.append(i)

        for i in range(len(result)):
            A[i] = result[i]

        return len(result)

    # 35. Reverse Linked List
    def reverse(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    # 174. Remove Nth Node From End of List
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)

        fast = head
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

    # 423. Valid Parentheses
    def is_valid_parentheses(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in pairs.keys():
                stack.append(ch)
            else:
                if len(stack) == 0 or pairs[stack[-1]] != ch:
                    return False
                else:
                    stack.pop()

        if len(stack) > 0:
            return False
        else:
            return True

    # 366. Fibonacci
    def fibonacci(self, n: int) -> int:
        f = [None for i in range(n + 1)]
        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n - 1]

    # 481. Binary Tree Leaf Sum (locked)
    def leafSum(self, root):
        result = []
        self.dfs(root, result)
        return sum(result)

    def dfs(self, root, result):
        if root is None:
            return

        if root.left is None and root.right is None:
            result.append(root.val)

        self.dfs(root.left, result)
        self.dfs(root.right, result)

    # 97. Maximum Depth of Binary Tree
    def max_depth(self, root: TreeNode) -> int:
        self.max_depth = 0
        self.traversal(root, 1)
        return self.max_depth

    def traversal(self, root, depth):
        if root is None:
            return

        if self.max_depth < depth:
            self.max_depth = depth

        self.traversal(root.left, depth + 1)
        self.traversal(root.right, depth + 1)

    # Identical Binary Tree

    # 66. Binary Tree Preorder Traversal
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

    def traversal(self, root, result):
        if root is None:
            return

        result.append(root.val)
        self.traversal(root.left, result)
        self.traversal(root.right, result)

    # 67. Binary Tree Inorder Traversal
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

    def traversal(self, root, result):
        if root is None:
            return

        self.traversal(root.left, result)
        result.append(root.val)
        self.traversal(root.right, result)

    # 68. Binary Tree Postorder Traversal
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

    def traversal(self, root, result):
        if root is None:
            return result

        self.traversal(root.left, result)
        self.traversal(root.right, result)
        result.append(root.val)

    # 6. Merge Two Sorted Arrays
    def mergeSortedArray(self, a: List[int], b: List[int]):
        index_a = 0
        index_b = 0
        result = []
        while index_a < len(a) and index_b < len(b):
            if a[index_a] < b[index_b]:
                result.append(a[index_a])
                index_a += 1
            else:
                result.append(b[index_b])
                index_b += 1

        while index_a < len(a):
            result.append(a[index_a])
            index_a += 1

        while index_b < len(b):
            result.append(b[index_b])
            index_b += 1

        return result


    # 464. Sort Integer II
    # 用 Merge sort
    def sort_integers2(self, a: List[int]):
        temp = [None for i in range(len(a))]
        self.merge_sort(a, 0, len(a) - 1, temp)

    def merge_sort(self, a: List[int], start: int, end: int, temp: List[int]):
        if start >= end:
            return

        mid = (start + end) // 2

        self.merge_sort(a, start, mid, temp)
        self.merge_sort(a, mid + 1, end, temp)
        self.merge_array(a, start, mid, end, temp)

    def merge_array(self, a: List[int], start: int, mid: int, end: int, temp: List[int]):
        left = start
        right = mid + 1
        idx = start

        while left <= mid and right <= end:
            if a[left] <= a[right]:
                temp[idx] = a[left]
                left += 1
            else:
                temp[idx] = a[right]
                right += 1
            idx += 1

        while left <= mid:
            temp[idx] = a[left]
            left += 1
            idx += 1

        while right <= end:
            temp[idx] = a[right]
            right += 1
            idx += 1

        for i in range(start, end + 1):
            a[i] = temp[i]

    # 用 Quick sort
    def sort_integers2(self, a: List[int]):
        self.quick_sort(a, 0, len(a) - 1)

    def quick_sort(self, a: List[int], start: int, end: int):
        if start >= end:
            return

        left = start
        right = end

        mid = (start + end) // 2
        pivot = a[mid]

        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left <= right:
                temp = a[left]
                a[left] = a[right]
                a[right] = temp
                left += 1
                right -= 1

        self.quick_sort(a, start, right)
        self.quick_sort(a, left, end)

    # 31. Partition Array
    def partitionArray(self, nums, k):
        if nums is None or len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1

        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        return start


    # Homework
    # 479. Second Max of Array
    def second_max(self, nums: List[int]) -> int:
        # return sorted(nums)[-2]
        max_1st = max(nums[0], nums[1])
        max_2nd = min(nums[0], nums[1])

        for i in range(2, len(nums)):
            if nums[i] > max_1st:
                max_2nd = max_1st
                max_1st = nums[i]
            elif nums[i] > max_2nd:
                max_2nd = nums[i]

        return max_2nd

    # 478. Simple Calculator (locked)
    def calculater(self, a, operator, b):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b

    # 283. Max of 3 Numbers
    def maxOfThreeNumbers(self, num1, num2, num3):
        return max(num1, num2, num3)

    # 145. Lowercase to Uppercase
    def lowercaseToUppercase(self, character):
        return character.upper()

    # 37. Reverse 3-digit Integer
    def reverse_integer(self, number: int) -> int:
        c = number % 10
        b = (number // 10) % 10
        a = (number // 100) % 10

        return c * 100 + b * 10 + a

    # 9. Fizz Buzz
    def fizzBuzz(self, n):
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('fizz buzz')
            elif i % 3 == 0:
                result.append('fizz')
            elif i % 5 == 0:
                result.append('buzz')
            else:
                result.append(str(i))

        return result
    
    # 483. Convert Linked List to Array List (locked)
    def toArrayList(self, head):
        result = []

        while head is not None:
            result.append(head.val)
            head = head.next

        return result

    # 225. Find Node in Linked List (locked)
    def findNode(self, head, val):
        while head is not None:
            if head.val == val:
                return head
            head = head.next

        return None

    # 219. Insert Node in Sorted Linked List (locked)
    def insertNode(self, head, val):
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next and curr.next.val < val:
            curr = curr.next

        node = ListNode(val, curr.next)
        curr.next = node

        return dummy.next

    # 452. Remove Linked List Elements
    def removeElements(self, head, val):
        dummy = ListNode(0, None)
        curr = dummy

        while head is not None:
            while head is not None and head.val == val:
                head = head.next
            curr.next = head
            curr = curr.next

            if head is not None:
                head = head.next

        return dummy.next

    # 241. String To Integer (locked)
    def stringToInteger(self, str):
        # return int(str)
        num, sign = 0, 1

        if str[0] == '-':
            sign = -1
            str = str[1:]

        for c in str:
            num = num * 10 + ord(c) - ord('0')

        return num * sign

    # 415. Valid Palindrome
    def is_palindrome(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True

        ch = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and s[i] not in ch:
                i += 1
            while i < j and s[j] not in ch:
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    # 174. Remove Nth Node From End of List
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)

        fast = head
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

    # 165. Merge Two Sorted Lists
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1 is not None:
            curr.next = l1
        if l2 is not None:
            curr.next = l2

        return dummy.next

    # 423. Valid Parentheses
    def is_valid_parentheses(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in pairs.keys():
                stack.append(ch)
            else:
                if len(stack) == 0 or pairs[stack[-1]] != ch:
                    return False
                else:
                    stack.pop()

        if len(stack) > 0:
            return False
        else:
            return True

    # 647. Find All Anagrams in a String (locked)
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []

        result = []


        hash = {}
        for ch in p:
            if ch in hash.keys():
                hash[ch] += 1
            else:
                hash[ch] = 1

        for i in range(len(p)):
            if s[i] in hash.keys():
                hash[s[i]] -= 1

        for i in range(len(s) - len(p) + 1):
            if i > 0:
                if s[i - 1] in hash.keys():
                    hash[s[i - 1]] += 1
                if s[i + len(p) - 1] in hash.keys():
                    hash[s[i + len(p) - 1]] -= 1

            if all(v == 0 for v in hash.values()):
                result.append(i)

        return result

    # 644. Strobogrammatic Number
    def is_strobogrammatic(self, num: str) -> bool:
        map_num = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        i = 0
        j = len(num) - 1

        while i <= j: # 注意要有等號
            if num[i] not in map_num.keys() or num[j] not in map_num.keys():
                return False
            elif map_num[num[i]] != num[j]:
                return False
            i += 1
            j -= 1

        return True

    # 557. Count Characters (locked)
    def countCharacters(self, str):
        hash = {}
        for c in str:
            if c in hash.keys():
                hash[c] += 1
            else:
                hash[c] = 1

        return hash

    # 457. Classical Binary Search
    def findPosition(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
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

    # 487. Name Deduplication (locked)
    def nameDeduplication(self, names):
        result = []

        d = {}
        for name in names:
            name = name.lower()
            if name not in d.keys():
                d[name] = 1
                result.append(name)

        return result

    # 481. Binary Tree Leaf Sum (locked)
    def leafSum(self, root):
        result = []
        self.dfs(root, result)
        return sum(result)

    def dfs(self, root, result):
        if root is None:
            return

        if root.left is None and root.right is None:
            result.append(root.val)

        self.dfs(root.left, result)
        self.dfs(root.right, result)

    # 480. Binary Tree Paths
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        result = []
        self.dfs(root, str(root.val), result)
        return result

    def dfs(self, root, curr_path, result):
        if root is None:
            return

        if root.left is None and root.right is None:
            result.append(curr_path)

        if root.left is not None:
            self.dfs(root.left, curr_path + '->' + str(root.left.val), result)
        if root.right is not None:
            self.dfs(root.right, curr_path + '->' + str(root.right.val), result)

    # 97. Maximum Depth of Binary Tree
    def max_depth(self, root: TreeNode) -> int:
        self.max_depth = 0
        self.traversal(root, 1)
        return self.max_depth

    def traversal(self, root, depth):
        if root is None:
            return

        if self.max_depth < depth:
            self.max_depth = depth

        self.traversal(root.left, depth + 1)
        self.traversal(root.right, depth + 1)

    # 376. Binary Tree Path Sum (locked)
    def binaryTreePathSum(self, root, target):
        result = []

        if root is None:
            return result

        self.helper(root, [root.val], )

    # 482. Binary Tree Level Sum (locked)
    def levelSum(self, root, level):
        result = []
        self.dfs(root, 1, result, level)
        return sum(p)

    def dfs(self, root, curr_level, result, target_level):
        if root is None:
            return

        if curr_level == target_level:
            result.append(root.val)

        self.dfs(root.left, curr_level + 1, result, target_level)
        self.dfs(root.right, curr_level + 1, result, target_level)

    # 463. Sort Integers
    def sort_integers(self, a: List[int]):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

    # 464. Sort Integers II
    # 用 Merge sort
    def sort_integers2(self, a: List[int]):
        temp = [None for i in range(len(a))]
        self.merge_sort(a, 0, len(a) - 1, temp)

    def merge_sort(self, a: List[int], start: int, end: int, temp: List[int]):
        if start >= end:
            return

        mid = (start + end) // 2

        self.merge_sort(a, start, mid, temp)
        self.merge_sort(a, mid + 1, end, temp)
        self.merge_array(a, start, mid, end, temp)

    def merge_array(self, a: List[int], start: int, mid: int, end: int, temp: List[int]):
        left = start
        right = mid + 1
        idx = start

        while left <= mid and right <= end:
            if a[left] <= a[right]:
                temp[idx] = a[left]
                left += 1
            else:
                temp[idx] = a[right]
                right += 1
            idx += 1

        while left <= mid:
            temp[idx] = a[left]
            left += 1
            idx += 1

        while right <= end:
            temp[idx] = a[right]
            right += 1
            idx += 1

        for i in range(start, end + 1):
            a[i] = temp[i]

    # 用 Quick sort
    def sort_integers2(self, a: List[int]):
        self.quick_sort(a, 0, len(a) - 1)

    def quick_sort(self, a: List[int], start: int, end: int):
        if start >= end:
            return

        left = start
        right = end

        mid = (start + end) // 2
        pivot = a[mid]

        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left <= right:
                temp = a[left]
                a[left] = a[right]
                a[right] = temp
                left += 1
                right -= 1

        self.quick_sort(a, start, right)
        self.quick_sort(a, left, end)

    # 173. Insertion Sort List
    def insertion_sort_list(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        dummy = ListNode(0, head)
        latest_sorted = head
        curr = head.next

        while curr is not None:
            if latest_sorted.val <= curr.val:
                latest_sorted = latest_sorted.next
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next

                latest_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr

            curr = latest_sorted.next

        return dummy.next

    # 184. Largest Number
    def largest_number(self, nums: List[int]) -> str:
        nums = sorted(nums, key=cmp_to_key(self.compare))
        if nums[0] == 0:
            return '0'
        else:
            return ''.join([str(i) for i in nums])

    def compare(self, a, b):
        if int(str(a) + str(b)) > int(str(b) + str(a)):
            return -1
        else:
            return

    # 148. Sort Colors
    def sort_colors(self, nums: List[int]):
        if nums is None or len(nums) == 0:
            return

        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

    # 143. Sort Colors II
    def sort_colors2(self, colors: List[int], k: int):
        if colors is None or len(colors) == 0:
            return

        self.rainbow_sort(colors, 0, len(colors) - 1, 1, k)

    def rainbow_sort(self, colors, start, end, color_from, color_to):
        if color_from == color_to:
            return

        if start >= end:
            return

        color_mid = (color_from + color_to) // 2
        left = start
        right = end

        while left <= right:
            while left <= right and colors[left] <= color_mid:
                left += 1
            while left <= right and colors[right] > color_mid:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.rainbow_sort(colors, start, right, color_from, color_mid)
        self.rainbow_sort(colors, left, end, color_mid + 1, color_to)

    # 139. Subarray Sum Closest (locked)
    def subarraySumClosest(self, nums):
        if nums is None or len(nums) == 0:
            return None

        pre_sum = [(0, -1)]
        for idx, val in enumerate(nums):
            sum = pre_sum[-1][0] + val
            pre_sum.append((sum, idx))

        pre_sum = sorted(pre_sum)

        closet = sys.maxsize
        result = []

        for i in range(1, len(pre_sum)):
            pre_sum_diff = pre_sum[i][0] - pre_sum[i - 1][0]
            if closet > pre_sum_diff:
                closet = pre_sum_diff
                start_index = min(pre_sum[i - 1][1], pre_sum[i][1]) + 1
                end_index = max(pre_sum[i - 1][1], pre_sum[i][1])
                result = [start_index, end_index]

        return result

    # 98. Sort List
    # 用 merge sort
    def sort_list(self, head:ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        h1 = self.sort_list(head)
        h2 = self.sort_list(mid)

        return self.merge_all(h1, h2)

    def merge_all(self, h1, h2):
        dummy = ListNode(0)
        curr = dummy

        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next

        if h1 is not None:
            curr.next = h1
        if h2 is not None:
            curr.next = h2

        return dummy.next

    # 用 Quick sort
    def sort_list(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow

        left_dummy, right_dummy, mid_dummy = ListNode(0), ListNode(0), ListNode(0)
        left_tail, right_tail, mid_tail = left_dummy, right_dummy, mid_dummy

        while head:
            if head.val < mid.val:
                left_tail.next = head
                left_tail = left_tail.next
            elif head.val > mid.val:
                right_tail.next = head
                right_tail = right_tail.next
            else:
                mid_tail.next = head
                mid_tail = mid_tail.next
            head = head.next

        left_tail.next = None
        right_tail.next = None
        mid_tail.next = None

        left = self.sort_list(left_dummy.next)
        right = self.sort_list(right_dummy.next)

        dummy = ListNode(0)
        tail = dummy

        while left:
            tail.next = left
            left = left.next
            tail = tail.next

        mid_curr = mid_dummy.next
        while mid_curr:
            tail.next = mid_curr
            mid_curr = mid_curr.next
            tail = tail.next

        while right:
            tail.next = right
            right = right.next
            tail = tail.next

        return dummy.next

    # 5. Kth Largest Element
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return -1

        nums = sorted(nums)
        if k <= len(nums):
            return nums[-k]
        else:
            return -1

# 495. Implement Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack = self.stack[:-1]

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

# 492. Implement Queue by Linked List
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        node = ListNode(item, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head is None and self.tail is None:
            return -1
        else:
            result = self.head.val
            self.head = self.head.next
            return result

# 454. Rectangle Area
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

# 222. Setter and Getter (locked)
class School:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

# 497. Shape Factory
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented')

class Triangle(Shape):
    def draw(self):
        print("  /\\")
        print(" /  \\")
        print("/____\\")

class Rectangle(Shape):
    def draw(self):
        print(" ----")
        print("|    |")
        print(" ----")

class Square(Shape):
    def draw(self):
        print(" ----")
        print("|    |")
        print("|    |")
        print(" ----")

class ShapeFactory:
    def getShape(self, shapeType):
        if shapeType == 'Square':
            return Square()
        elif shapeType == 'Triangle':
            return Triangle()
        elif shapeType == 'Rectangle':
            return Rectangle()

# 455. Student ID (locked)
class Student:
    def __init__(self, id):
        self.id = id

class Class:
    def __init__(self, n):
        self.students = []
        for i in range(n):
            self.students.append(Student(i))

# 218. Student Level (locked)
class Student:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def getLevel(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'D'

# 40. Implement Queue by Two Stacks
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        self.stack1.append(element)

    def pop(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        result = self.stack2.pop()

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        return result

    def top(self):
        return self.stack1[0]

# 494. Implement Stack by Two Queues (locked)
import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()

    def push(self, x):
        self.queue1.put(x)

    def pop(self):
        while self.queuq1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        item = self.queue1.get()
        self.quque1, self.queue2 = self.queue2, self.quque1

    def top(self):
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.push(item)
        return item

    def isEmpty(self):
        return self.queue1.empty()
