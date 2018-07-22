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

    def startFind(self, thing):
        ''' returns BSTnode if found, else returns None -- this is the helper function '''
        if self.isEmpty():
            return None
        else:
            return self.find(thing, self.root)

    def find(self, thing, node):
        ''' this is the recursive function '''
        if node.getData() == thing :
            print ("found it")
            return node
        if thing < node.getData() :
            if node.getLeft() == None:
                print("sorry -- the thing = " +str(thing)+ " wasn't there :(")
                return None
            return self.find(thing, node.getLeft())
        else :
            if node.getRight() == None:
                print("sorry -- the thing = " +str(thing)+ " wasn't there :(")
                return None
            return self.find(thing, node.getRight())

    def startOrderedList(self):
        temp = []
        if self.isEmpty():
            print("The tree was empty")
            return temp
        else:
            return self.getOrderedList(temp, self.root)

    def getOrderedList(self, tempList, node):
        if node.hasLeft():
            tempList = self.getOrderedList(tempList, node.getLeft())
        tempList.append(node.getData())
        if node.hasRight():
            tempList = self.getOrderedList(tempList, node.getRight())
        return tempList


