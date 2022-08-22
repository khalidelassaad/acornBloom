class Tree:
    agesDict = {} # define tree stages and age milestones here
    
    '''
    DIRECTIONS:
        incoming:
            -\|/-
            54321
        outgoing:
            12345
            -/|\-
    '''
    rootDirectionsToSymbol = {
        1: "-",
        2: "/",
        3: "|",
        4: "\\",
        5: "-",
    }

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.age = 0
        self.treeShapeDict = {
            (0,0): {
                "type": {
                    "origin" : None,
                    "root" : {
                        "incomingDirection" : 3,
                        "outgoingPossibilities": [1, 2, 3, 4, 5],
                        "outgoingBranches" : 0
                    }
                },
                "symbol": "@"
            }
        }

    def getCoords(self):
        return (self.y, self.x)

    def ageOneYear(self):
        self.age += 1
        self.handleAging()
        return self.age

    def handleAging(self):
        if self.age % 100 == 0:
            self.addRootSegment

    def addRootSegment(self):
        rootToGrowFrom = self.getRandomRootSegment()
        rootToGrowFrom.
    
    def getTreePieces(self):
        return self.treeShapeDict.items()