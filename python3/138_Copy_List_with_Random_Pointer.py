class Solution(object):
    # 方法1:
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        
        # 1. copy nodes
        self.copy_nodes(head)
        # 2. copy random
        self.copy_random(head)
        
        return self.split_list(head)
        
    # 邊掃描 1->2->3->4 邊拷貝節點建立成 1->1'->2->2'->3->3'->4->4'
    def copy_nodes(self, head):
        while head is not None:
            # 拷貝節點
            node = RandomListNode(head.label)
            node.next = head.next
            node.random = head.random # 這時候 node 的 random 並不是我要的結果
            
            # 把拷貝的節點接上原本的 list
            head.next = node
            # 再把 head 移動到原本 list 中的下一個節點
            head = head.next.next
            
    def copy_random(self, head):
        while head != None:
            if head.next.random != None: # head.next 就是指向新拷貝的節點
                head.next.random = head.random.next
            head = head.next.next
            
    def split_list(self, head):
        new_head = head.next
        while head != None:
            curr = head.next
            head.next = curr.next # 把原先 list 中的下一個接回來
            head = head.next # 移動到下一個原先 list 中的節點
            
            if curr.next != None: # curr 有可能是在原先加上拷貝過後的 list 中的最後一個
                curr.next = curr.next.next
        return new_head

class Solution(object):
    # 方法2: 用 hash map
    def copyRandomList(self, head):
        self.dummy = RandomListNode(0)
        self.curr = self.dummy
        self.hash_map = {}
        
        while head != None:
            if head in self.hash_map:
                new_node = self.hash_map[head] # 因為第 65 行也可能把節點的關係放到 hash_map 中，所以可能 hash_map 中已經存在了
            else:
                new_node = RandomListNode(head.label)
                self.hash_map[head] = new_node
            self.curr.next = new_node
            
            if head.random is not None:
                if head.random in self.hash_map:
                    new_node.random = self.hash_map[head.random]
                else:
                    new_node.random = RandomListNode(head.random.label)
                    self.hash_map[head.random] = new_node.random
                    
            # curr 和 head 個往下移動一格
            self.curr = new_node
            head = head.next
            
        return self.dummy.next

class Solution(object):
    # 方法3:
    def copyRandomList(self, head):
        # write your code here
        if head == None:
            return None
            
        myMap = {}
        nHead = RandomListNode(head.label) # 新節點的頭
        myMap[head] = nHead
        p = head
        q = nHead
        while p != None:
            q.random = p.random # 先把原先節點的 random 暫時分配給新節點，等一下再修改
            if p.next != None:
                q.next = RandomListNode(p.next.label)
                myMap[p.next] = q.next
            else:
                q.next = None
            p = p.next
            q = q.next
        
        p = nHead # 這時後 p 是指向新的 linked list 的元素
        while p!= None:
            if p.random != None:
                p.random = myMap[p.random] # 把新節點的 random 修改成正確的
            p = p.next
        return nHead
        
# lintcode 105
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return head
        # 先複製節點，插入到原本的節點後面
        curr = head
        while curr:
            node = RandomListNode(curr.label)
            temp = curr.next
            curr.next = node
            node.next = temp
            curr = curr.next.next
            
        # 複製 random 指標指的東西
        curr = head
        while curr:
            new_node = curr.next
            if curr.random is not None:
                new_node.random = curr.random.next
            curr = curr.next.next

        new_head = head.next
        curr = head.next
        while curr.next:
            curr.next = curr.next.next
            curr = curr.next
            
        return new_head
        
    def copyRandomList(self, head):
        # 用 hash map 來記錄新舊節點
        hash_map = {}
        curr = head
        while curr:
            node = RandomListNode(curr.label)
            node.next = curr.next
            node.random = curr.random
            hash_map[curr] = node # key 是舊的節點，val 是新的節點
            curr = curr.next
            
        curr = head
        while curr:
            new_node = hash_map[curr]
            if curr.next is not None:
                new_node.next = hash_map[curr.next]
            if curr.random is not None:
                new_node.random = hash_map[curr.random]
            curr = curr.next
                
        return hash_map[head]
