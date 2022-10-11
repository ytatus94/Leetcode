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
            print(curr_level)
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

# 方法2: 比較快
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
            print(curr_layer)
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
