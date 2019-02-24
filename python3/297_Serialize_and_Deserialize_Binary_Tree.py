# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '{}'
        
        # 首先把起點放到 queue
        queue = [root]
        
        index = 0 # 用來表存取 queue 中的某個元素
        
        while index < len(queue):
            if queue[index] is not None: # 如果本身是空節點，就不會再有左右子樹了
                queue.append(queue[index].left)
                queue.append(queue[index].right)
                # 這邊有可能 queue[index] 是葉子節點
                # 所以會把空節點塞入 queue 中
            index += 1
        
        # 如果最後遇到了葉子節點，那葉子節點後面會塞入一堆空節點
        # 要把空節點拿掉
        while queue[-1] is None:
            queue.pop()
            
        # 在輸出時把元素之間以逗號連接
        # 如果遇到空節點用 # 取代
        return '{%s}' % ','.join(str(node.val) if node is not None else '#' for node in queue)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('\n')
        
        if data == '{}':
            return None

        # 此時 data 是 '{1', '2', '3', '#', '#', '4', '5}'
        # 所以要先把最左邊的 { 和最右邊的 } 拿掉
        vals = data.lstrip('{').rstrip('}').split(',')
        
        # 樹的根節點是第一個元素
        root = TreeNode(int(vals[0]))
        queue = [root]
        index = 0 # 用來控制現在要處理哪一個節點
        is_left = True # 用來切換左右子樹
        
        # 剩下的元素兩兩一組，分別是左右子樹
        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if is_left:
                    queue[index].left = node
                else:
                    queue[index].right = node
                    
                queue.append(node)
        
            # 如果剛剛接上的是右子樹，表示要移動到下一個節點了
            # 注意這一步要再切換左右子樹開關之前才不會出錯
            if not is_left:
                index += 1
            
            # 接完了一個子樹後，要切換左右子樹的開關
            is_left = not is_left

        return root

        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
