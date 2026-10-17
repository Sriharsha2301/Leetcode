# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def preorder(self,node):
        if not node:
            self.l.append("#")
            return None
        self.l.append(str(node.val))
        self.preorder(node.left)
        self.preorder(node.right)
   
      
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.l=[]
        self.preorder(root)
        return "/".join(self.l)
                 
    def build(self):
        if self.l[self.i]=="#":
            self.i+=1
            return None
        node=TreeNode(int(self.l[self.i]))
        self.i+=1

        node.left=self.build()
        node.right=self.build()
        return node
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.l=data.split("/")
        self.i=0
        return self.build()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans