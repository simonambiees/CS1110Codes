class BSTNode :
    numMade = 0

    def __init__(self, data = None, L = None, R = None):
        self.data = data
        self.left = L
        self.right = R
        self.ID = BSTNode.numMade
        BSTNode.numMade += 1

    def getID(self): return self.ID

    def setData(self, data): self.data = data
    def getData(self): return self.data

    def setLeft(self, L): self.left = L
    def getLeft(self): return self.left

    def setRight(self, R): self.right = R
    def getRight(self): return self.right

    def showInfo(self):
        tempInfo = "node_(" + str(self.ID) + ") "
        tempInfo += "\t= << " + str(self.data) + " >> "
        if self.left == None:
            tempInfo += "\tL = None "
        else:
            tempInfo += "\tL = node_(" + str(self.left.getID()) + ") "
        if self.right == None:
            tempInfo += ", R = None "
        else:
            tempInfo += ", R = node(" + str(self.right.getID()) + ")"
        return tempInfo