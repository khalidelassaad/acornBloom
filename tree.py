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

    rootDirectionsToOutgoingDisplacement = {
        1: (0, -1),
        2: (1, -1),
        3: (1, 0),
        4: (1, 1),
        5: (0, 1)
    }

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.age = 0
        self.treeDict = {
            (0,0): {
                "type": {
                    "origin" : None,
                    "root" : {
                        "incomingDirection" : 3,
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
        if self.age % 10 == 0:
            self.growOneRootSegment()

    def getGrowableRootSegments(self):
        candidates = []
        for coords, data in self.treeDict.items():
            pieceType = data["type"]
            if "root" in pieceType:
                if pieceType["root"]["outgoingBranches"] < 3:
                    possibilities = self.getOutgoingRootPossibilities(coords)
                    if possibilities:
                        candidates.append((coords, possibilities))
        return candidates

    def createRootSegmentInTreeDict(self, newCoords, growDirection):
        self.treeDict[newCoords] = {
                "type": {
                    "root" : {
                        "incomingDirection" : growDirection,
                        "outgoingBranches" : 0
                    }
                },
                "symbol": Tree.rootDirectionsToSymbol[growDirection]
            }

    def getOutgoingRootPossibilities(self, rootCoords):
        possibleDirections = [1,2,3,4,5]
        returnList = []
        for possibleDirection in possibleDirections:
            displacement = Tree.rootDirectionsToOutgoingDisplacement[possibleDirection]
            newY = rootCoords[0] + displacement[0]
            newX = rootCoords[1] + displacement[1]
            if (newY, newX) not in self.treeDict:
                returnList.append(possibleDirection)
        return returnList

    def growOneRootSegment(self):
        candidates = self.getGrowableRootSegments()
        candidateCoords, possibilities = random.choice(candidates)
        candidate = self.treeDict[candidateCoords]

        growDirection = random.choice(possibilities)

        # Grow from old segment
        #   Increment old segment's branch counter
        candidate["type"]["root"]["outgoingBranches"] += 1

        # Grow new segment
        #   Calculate new coords (with old coords + direction)
        displacement = Tree.rootDirectionsToOutgoingDisplacement[growDirection]
        newY = candidateCoords[0] + displacement[0]
        newX = candidateCoords[1] + displacement[1]
        newCoords = (newY, newX)
        #   Add a new tree piece
        self.createRootSegmentInTreeDict(newCoords, growDirection)
    
    def getTreeDictItems(self):
        return self.treeDict.items()