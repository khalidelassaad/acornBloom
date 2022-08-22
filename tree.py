import math
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
        1: "_",
        2: "/",
        3: "|",
        4: "\\",
        5: "_",
    }

    rootDirectionsToInitialPossibilities = {
        1: [1,2],
        2: [1,2,3],
        3: [2,4],
        4: [3,4,5],
        5: [4,5]
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
        self.rootsLeft = 0
        self.rootsRight = 0

    def getCoords(self):
        return (self.y, self.x)

    def ageOneYear(self):
        self.age += 1
        self.handleAging()
        return self.age

    def handleAging(self):
        if self.age % 1 == 0:
            self.growOneRootSegment()

    def isThereRootAtCoords(self, coords):
        if not self.treeDict.get(coords):
            return False
        return "root" in self.treeDict.get(coords)["type"]

    def isRootTooCrowded(self, coords):
        numberOfNeighbors = 0
        displacements = [-1, 0, 1]
        for i in displacements:
            for j in displacements:
                if i == 0 and j == 0:
                    continue
                if self.isThereRootAtCoords((coords[0] + i, coords[1] + j)):
                    numberOfNeighbors += 1
        return numberOfNeighbors > 3


    def getGrowableRootSegments(self):
        candidates = []
        # TODO: split check on density of original root segments
        for coords, data in self.treeDict.items():
            if self.isRootTooCrowded(coords):
                continue
            pieceType = data["type"]
            if "root" in pieceType:
                if pieceType["root"]["outgoingBranches"] < 3:
                    possibilities = self.getOutgoingRootPossibilities(coords)
                    if possibilities:
                        candidates.append((coords, possibilities))
        return candidates

    def createRootSegmentInTreeDict(self, newCoords, growDirection):
        if newCoords[1] > 0:
            self.rootsRight += 1
        elif newCoords[1] < 0:
            self.rootsLeft += 1
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
        oldDirection = self.treeDict[rootCoords]["type"]["root"]["incomingDirection"]
        possibleDirections = Tree.rootDirectionsToInitialPossibilities[oldDirection]
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

        # Encourage: Far growth!
        if random.random() < 0.5:
            candidates.sort(key = lambda x: math.dist(x[0], (0,0)))
            candidates = candidates[ - ( len(candidates)-1 ) // 3:]

        # Encourage: Balancing growth!
        if random.random() < 0.3:
            candidates.sort(key = lambda x: x[0][1], reverse = self.rootsLeft < self.rootsRight)
            candidates = candidates[ - ( len(candidates)-1 ) // 4:]

        # Encourage: Outward growth!
        if random.random() < 0.2:
            candidates.sort(key = lambda x: abs(x[0][1]))
            candidates = candidates[ - ( len(candidates)-1 ) // 2:]

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