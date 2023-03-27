# 這題也是層及遍歷，用 BFS
# 用 Binary Tree Level Order Traversal 模板先找出每一層的元素
# 每一層的元素會組成一個 linked list 所以有 n 層就會有 n 個 linked list
# 找出每一層的元素後，用這些元素組成一個 linked list 再塞到 results 裡面

# 方法1: 用 Binary Tree Level Order Traversal 的模板
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        results = []
        if root is None:
            return results

        queue = [root]

        while queue:
            curr_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 這上面的部分就和 Binary Tree Lever Order Traversal 一樣
            # 找出該層所有元素後，把這些元素組成一個 linked list 再放到 results 裡面
            head = self.list_to_linkedlist(curr_level)
            results.append(head)

        return results

    def list_to_linkedlist(self, nums):
        dummy = ListNode(0, None)
        curr = dummy
        for i in range(len(nums)):
            new_node = ListNode(nums[i], None)
            curr.next = new_node
            curr = curr.next
        return dummy.next

# 方法2: 比較快，因為一邊找出每一層的元素，一邊建立 linked list
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        results = []

        if root is None:
            return results

        queue = [root]

        dummy = ListNode(0, None)
        curr = None

        while queue:
            curr = dummy
            for i in range(len(queue)):
                node = queue.pop(0)
                curr.next = ListNode(node.val, None)
                curr = curr.next

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            results.append(dummy.next)

        return results

# 方法3:
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root is None:
            return []

        results = []
        queue = [root]
        while queue:
            # 現在這層的節點
            curr_layer = [node.val for node in queue]
            head = self.convert_list_to_linked_list(curr_layer)
            results.append(head)
            
            # 把下一層的結點加入到 queue 中
            next_layer = []
            for node in queue:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            queue = next_layer
        return results

    def convert_list_to_linked_list(self, nums):
        dummy_node = ListNode(0, None)
        curr = dummy_node
        for i in nums:
            curr.next = ListNode(i, None)
            curr = curr.next
        return dummy_node.next
