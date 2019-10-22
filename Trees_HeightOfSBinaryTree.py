#class Node:
#      def __init__(self,info): 
#          self.info = info  
#          self.left = None  
#          self.right = None 
#this is a node of the tree , which contains info as data, left , right

def height(root):
    def _height(root):
        lh = 0
        rh = 0
        if root.left:
            lh = 1 + _height(root.left)
        if root.right:
            rh = 1 + _height(root.right)
        return max(1, lh, rh)
    return _height(root) - 1