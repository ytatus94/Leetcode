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
