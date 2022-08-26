import random

from utility import coordsAdd


class BranchNode:
    mapDirectionToSymbol = {
        0: "/",
        1: "-",
        2: "\\",
        3: "|",
        4: "/",
        5: "-",
        6: "\\"
    }

    def __init__(self, direction, growthChildren=[], branchChildren=[]):
        self.direction = direction
        self.growthChildren = growthChildren
        self.branchChildren = branchChildren

    def hasBranched(self):
        return not not self.branchChildren

    def hasGrown(self):
        return not not self.growthChildren

    def getSymbol(self):
        return BranchNode.mapDirectionToSymbol[self.direction]


class Branches:
    # DIRECTIONS:
    #     2 3 4
    #      \|/
    #    1 -+- 5
    #      / \
    #     0   6

    mapDirectionToBranchDirections = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4, 6],
        6: [5]
    }

    mapGrowthDirectionToCoordDelta = {
        0: (1, -1),
        1: (0, -1),
        2: (-1, -1),
        3: (-1, 0),
        4: (-1, 1),
        5: (0, 1),
        6: (1, 1)
    }

    mapBranchDirectionToCoordDelta = {
        (0, 1): (0, -1),
        (1, 0): (1, -1),
        (1, 2): (-1, -1),
        (2, 1): (0, -1),
        (2, 3): (-1, 0),
        (3, 2): (-1, -1),
        (3, 4): (-1, 1),
        (4, 3): (-1, 0),
        (4, 5): (0, 1),
        (5, 4): (-1, 1),
        (5, 6): (1, 1),
        (6, 5): (0, 1)
    }

    def __init__(self, branchOriginDataDict):
        leftBranchNode = BranchNode(2)
        rightBranchNode = BranchNode(4)

        self.rootBranchNode = BranchNode(
            3, branchChildren=[leftBranchNode, rightBranchNode])
        self.branchOriginDataDict = branchOriginDataDict

    def handleAging(self):
        pass

    def _recursiveBranchDict(self, coords, branchNode: BranchNode):
        returnDict = dict()
        # if children, call this function on them with THEIR coords and THEIR branch node,
        # and assemble returned dicts into returndict
        if branchNode.hasGrown():
            # handle grownChildren
            for growthChildNode in branchNode.growthChildren:
                coordDelta = Branches.mapGrowthDirectionToCoordDelta[branchNode.direction]
                newCoords = coordsAdd(coords, coordDelta)
                returnDict.update(self._recursiveBranchDict(
                    newCoords, growthChildNode))
        if branchNode.hasBranched():
            # handle branchChildren
            for branchChildNode in branchNode.branchChildren:
                coordDelta = Branches.mapBranchDirectionToCoordDelta[(
                    branchNode.direction, branchChildNode.direction)]
                newCoords = coordsAdd(coords, coordDelta)
                returnDict.update(self._recursiveBranchDict(
                    newCoords, branchChildNode))

        # Base Case & Recursive case: return dict containing coords->{"symbol":branchNode symbol}
        returnDict[coords] = {"symbol": branchNode.getSymbol()}
        return returnDict

    def getBranchDict(self):
        return self._recursiveBranchDict((0, 0), self.rootBranchNode)
