"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    方法1:
    def rehashing(self, hashTable):
        # write your code here
        if len(hashTable) <= 0:
            return hashTable
        
        # 建立一個新的 hash table
        # 長度是原來的兩倍，全部填滿 None
        new_capacity = 2 * len(hashTable)
        new_hash_table = [None for i in range(new_capacity)]
        
        # 開始讀取原先的 hash table
        for item in hashTable:
            # 原先的 hash table 中的 item 也有可能是 linked list
            # 所以要用 while loop 跑全部的節點
            while item is not None:
                # 換算出要放在新的 hash table 中的哪個位置
                new_index = (item.val % new_capacity + new_capacity) % new_capacity
                
                if new_hash_table[new_index] is None:
                    # 如果是空的就當成 ListNode 直接塞入
                    new_hash_table[new_index] = ListNode(item.val)
                else:
                    # 如果不是空的就是變成 linked list 塞到最後一個
                    curr = new_hash_table[new_index]
                    while curr.next:
                        # 先移動到目前 linked list 中的最後一個 node
                        curr = curr.next
                    curr.next = ListNode(item.val)
                
                # 
                item = item.next
    
        return new_hash_table

class Solution:
    # 方法2: 拆成三個函數，每個函數負責不同的功能
    def rehashing(self, hashTable):
        new_capacity = 2 * len(hashTable)
        new_hash_table = [None for i in range(new_capacity)]
        for item in hashTable:
            while item != None:
                # 在新的 hash table 中插入值
                self.add_node(new_hash_table, item.val)
                item = item.next
        return new_hash_table
        
    def add_node(self, new_hash_table, value):
        # 換算成在新的 hash table 中的 index
        index = value % len(new_hash_table)
        if new_hash_table[index] == None:
            new_hash_table[index] = ListNode(value)
        else:
            self.add_listnode(new_hash_table[index], value)
            
    def add_listnode(self, node, value):
        if node.next == None:
            node.next = ListNode(value)
        else:
            self.add_listnode(node.next, value)
