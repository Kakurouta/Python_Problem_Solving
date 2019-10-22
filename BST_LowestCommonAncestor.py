#class Node:
#      def __init__(self,info): 
#          self.info = info  
#          self.left = None  
#          self.right = None 
#this is a node of the tree , which contains info as data, left , right

def lca(root, v1, v2):
    s = min(v1, v2)
    m = max(v1, v2)
    ans = root
    if s > ans.info:
        while s > ans.info:
            ans = ans.right
    elif m < ans.info:
        while m < ans.info:
            ans = ans.left
    return ans