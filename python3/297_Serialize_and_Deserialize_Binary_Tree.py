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

# lintcode 7
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if root is None:
            return '{}'
            
        q = [root]
        res = []
        
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                res.append(node)
                if node is not None:
                    q.append(node.left)
                    q.append(node.right)
            
        while res[-1] is None:
            res.pop()
            
        res = [str(node.val) if node is not None else '#' for node in res]

        return '{%s}' % ','.join(res)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data == '{}':
            return None
        
        data = data.lstrip('{')
        data = data.rstrip('}')
        data = data.split(',')
        
        root = TreeNode(int(data[0]))
        q = [root]
        index = 0
        is_left = True
        
        for i in data[1: ]:
            if i is not '#':
                node = TreeNode(int(i))
                q.append(node)
                if is_left:
                    q[index].left = node
                else:
                    q[index].right = node
                    
            if not is_left:
                index += 1
            is_left = not is_left
            
        return root
