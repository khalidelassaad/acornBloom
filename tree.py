class Tree:
    agesDict = {} # define tree stages and age milestones here
    


    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.age = 0
        self.treeShapeDict = {
            (0,0): "@"
        }

    def getCoords(self):
        return (self.y, self.x)

    def ageOneYear(self):
        self.age += 1
        return self.age
    
    def getTreePieces(self):
        return self.treeShapeDict.items()