import sys

sys.setrecursionlimit(5000)

class BinaryTree:
    def __init__(self, root, depth):
        self.root = root
        self.lchild = None
        self.rchild = None
        self.depth = depth
    def setl(self, tree):
        self.lchild = tree
    def setr(self, tree):
        self.rchild = tree
    def getl(self):
        return self.lchild
    def getr(self):
        return self.rchild
    def rootv(self):
        return self.root
    def swap(self):
        self.lchild, self.rchild = self.rchild, self.lchild


def swapNodes(indexes, queries):
    def inorder(btree, arr):
        if btree:
            inorder(btree.getl(), arr)
            arr.append(btree.root)
            inorder(btree.getr(), arr)
        return arr

    tree = BinaryTree(1, 1)
    treestack = []
    treestack.append(tree)

    for nodes in indexes:
        if nodes[0] != -1:
            treestack.append(BinaryTree(nodes[0], 1))
        if nodes[1] != -1:
            treestack.append(BinaryTree(nodes[1], 1))
    i = 0
    j = 0
    for t in treestack:
        if indexes[i][0] != -1:
            t.setl(treestack[j+1])
            treestack[j+1].depth = t.depth + 1
            j += 1
        if indexes[i][1] != -1:
            t.setr(treestack[j+1])
            treestack[j+1].depth = t.depth + 1
            j += 1
        i += 1
    ans = []
    for k in queries:
        for tr in treestack:
            if tr.depth%k == 0:
                tr.swap()
        ans.append(inorder(tree,[]))
        
    return ans
