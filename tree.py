import random

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
            self.addRootSegment()

    def getGrowableRootSegments(self):
        candidates = []
        for coords, data in self.treeShapeDict:
            pieceType = data["type"]
            if "root" in pieceType:
                if pieceType["root"]["outgoingBranches"] < 3:
                    if pieceType["root"]["outgoingPossibilities"]:
                        candidates.append(coords)
        return candidates

    def addRootSegment(self):
        candidates = self.getGrowableRootSegments()
        candidate = random.choice(candidates)
        possibilities = candidate["outgoingPossibilities"]
        growDirection = random.choice(possibilities)
        # Grow from old segment
        #   Eliminate possibility that we claimed
        possibilities.remove(growDirection)
        #   Increment old segment's branch counter
        candidate["outgoingBranches"] += 1
        # Grow new segment
        #   Calculate new coords (with old coords + direction)
        #   Add a new tree piece
        #   Give it the correct root data (incoming branch and check all possible directions for root)

    
    def getTreePieces(self):
        return self.treeShapeDict.items()