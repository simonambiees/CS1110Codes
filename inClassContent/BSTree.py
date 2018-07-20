from BSTNode import BSTNode

class BSTree:

    def __init__(self):
        self.root = BSTNode() ## creates an empty node ab initio
        self.size = 0 ## to hold the number of actual data terms in the tree
        self.allNodes = [] ## a temporary fudge to hold all the tree's nodes
        self.allNodes.append(self.root) ## initially doesn't hold anything

    def isEmpty(self): return self.size == 0

    def include(self, D): ## the helper function for the recursive insert function
        ''' this inserts D into the correct place in the Binary Search Tree '''
        if self.isEmpty() :
            self.root.setData(D) ##### = BSTNode(D)
            self.size += 1
        else :
            self.insert(D, self.root)

    def insert(self, d, node):
        ## presuming node not bad
        if d < node.getData() :
            if node.getLeft() != None :
                self.insert(d, node.getLeft())
            else :
                node.setLeft( BSTNode(d) )
                self.size += 1
                self.allNodes.append( node.getLeft() )
        else :
            if node.getRight() != None :
                self.insert(d, node.getRight())
            else :
                node.setRight( BSTNode(d) )
                self.size += 1
                self.allNodes.append( node.getRight() )

    def showTree(self):
        if self.isEmpty():
            return "Sorry, this tree is empty"
        else:
            tempInfo = "My tree has:\n"
            for node in self.allNodes:
                tempInfo += "\t" + node.showInfo() +"\n"
            return tempInfo
