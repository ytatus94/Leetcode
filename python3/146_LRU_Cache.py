# 用 singl linked list
class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
            
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash = {}
        self.dummy = ListNode(0, 0)
        self.tail = self.dummy # 這時候 dummy 和 tail 指向同一個 node
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash:
            return -1
        
        # LRU 就像一個按時間排序的序列，剛存取的就放在最尾端
        # 越前方表示越早之前存取的
        # 用 get() 去存取 key，如果 key 存在的話，把 key 搬到最尾端
        self.move_to_tail(key)
        
        # 因為 key 已經被搬到最尾端了所以是回傳 tail 的 value
        return self.tail.val

    # 用來把 prev->curr->n1->...->tail->None
    # 變成 prev->n1->...->tail->curr->None
    def move_to_tail(self, key):
        # 用 singly linked list 時 hash 中 key 要紀錄的是 current node 的上一個節點
        prev = self.hash[key] # key 是 curr 的 key
        curr = prev.next
        
        # 如果要找的節點正好是最後一個，那就什麼都不做
        if curr == self.tail:
            return
        
        # 如果要找的節點不是最後一個，那要把它移到最後面
        prev.next = curr.next # 把 prev.next 指向 n1
        self.tail.next = curr
        curr.next = None
        
        # 這時候 prev.next 已經是 n1 了
        # curr 的前一個也變成 tail 了，所以要更新 hash table
        if prev.next is not None:
            # n1 是 prev.next，所以 prev.next.key 是 n1 的 key
            self.hash[prev.next.key] = prev # n1 的 key 要存的是上一個節點
        
        self.hash[curr.key] = self.tail
        # 然後再把 tail 指向目前是最後一個元素的 curr
        self.tail = curr
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # 先看看 key 存不存在 hash 中
        # 如果存在，就把 node 搬到最尾端，並更新 node 的值
        if key in self.hash:
            prev = self.hash[key]
            curr = prev.next
            curr.val = value # 更新 node 的值
            self.move_to_tail(key) # 搬到最尾端
        else: # 如果不存在，就塞到最後面
            node = ListNode(key, value)
            self.hash[key] = self.tail
            self.tail.next = node
            self.tail = node # 把 tail 指標移動到最後一個節點
            # 但是塞到後面後可能造成 hash 的大小比 capacity 大
            # 這時候要把第一個 (最不常用的那個) 刪掉
            if len(self.hash) > self.capacity:
                first_node = self.dummy.next
                second_node = first_node.next
                # 在 hash 表格中要先移除第一個點的 key (指向 dummy)
                # 這樣就無法藉由 hash 來找到第一個點
                del self.hash[first_node.key]
                # 把 dummy 的下一個指向第二個節點
                # 如此一來就移除了第一個節點
                self.dummy.next = second_node
                self.hash[second_node.key] = self.dummy

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# lintcode 134
# 實作 LRU cache 可以用 oping hashing
# open hashing 每個位置是一個 linked list
# 所以要先定義一個 linked list 類別
# 又可以分成用 singly linked list 或是 doubly linked list 兩種
# 這邊用 doubly linked list 的方式
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.hash_map = {} # key 是 node 的 key, val 是 node 本身 (不是節點的值)
        
        # 建立 head 和 tail 兩個 dummy nodes
        # head 永遠是第一個，tail 永遠是最後一個，然後在這個 head tail 組成的 linked list 裡面沒有 null 結尾
        # 會是這樣的形式head->(n1->n2->n3->...->nk)->tail
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.hash_map:
            return -1
        
        # 因為是 linked list 所以當 node 存在的時候
        # 要把 node 從 linked list 當前位置移除，然後放到最末端
        curr = self.hash_map[key] # 得到 key 所代表的節點
        
        # 要把 prev->curr->next->...->n_last(tail.prev)->tail
        # 改成 prev->next->...->n_last->curr->tail
        # 和用 singly linked list 方法不同的是，這邊的 tail 永遠是 dummy 的，永遠放在最尾巴方便存取
        prev = curr.prev
        next = curr.next
        
        prev.next = next
        next.prev = prev
        
        curr.prev = self.tail.prev
        self.tail.prev = curr
        curr.prev.next = curr
        curr.next = self.tail
        
        # 把 key 對應到的 node 的值傳回
        return self.hash_map[key].val
            

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        # 會用到 set 函數表示
        # 1. 要改變 key 對應到的節點的值
        # 2. 或是 key 對應到的節點不在 hash_map 裡面，所以要把當前節點加入 hash_map，和 linked list 裡面
        
        # 情形1:
        # 有可能 key 存在，但是 value 不同
        # 所以要把原先的 value 改成餵給 set 函數的 value
        if self.get(key) != -1:
            # 執行過 self.get(key) 後 key 對應的節點會被移動到 linked list 最末端
            # 所以直接修改值就好
            self.hash_map[key].val = value
            return
        
        # 情形2:
        # key 不存在，所以要加入該節點
        # 可是加入之前要先判斷 hash_map 大小是否夠大
        # 如果已經滿了，就要先把 linked list 的第一個元素移除
        # 然後再加入新的節點到 linked list 的尾巴
        if len(self.hash_map) == self.capacity:
            first_node = self.head.next
            second_node = self.head.next.next
            del self.hash_map[first_node.key]
            self.head.next = second_node
            second_node.prev = self.head
            
        node = ListNode(key, value)
        self.hash_map[key] = node
        
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail
