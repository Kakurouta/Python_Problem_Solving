#Node is defined as
#class node:
#    def __init__(self, data):
#        self.data = data
#        self.left = None
#        self.right = None

def checkBST(root):
    seen = {}
    ma = root.data
    mi = root.data
    a = root
    b = root
    while a.right:
        ma = max(ma, a.right.data)
        a = a.right
    while b.left:
        mi = min(mi, b.left.data)
        b = b.left
    def _checkBST(root, seen, ma, mi):
        if root.data in seen:
            return False
        else:
            seen[root.data] = 1 
            if not root.left and not root.right:
                return True 
            if root.right and root.left:
                r = mi <= root.data < root.right.data <= ma
                l = ma >= root.data > root.left.data >= mi
                rr = _checkBST(root.right, seen, ma, max(mi, root.data))
                ll = _checkBST(root.left, seen, min(ma, root.data), mi)             
                return r and rr and l and ll                
            elif root.right:
                r = mi <= root.data < root.right.data <= ma
                rr = _checkBST(root.right, seen, ma, max(mi, root.data))
                return r and rr
            elif root.left:
                l = ma >= root.data > root.left.data >= mi
                ll = _checkBST(root.left, seen, min(ma, root.data), mi) 
                return l and ll

    return _checkBST(root, seen, ma, mi)