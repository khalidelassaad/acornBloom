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

    def __init__(self, direction, growthChildren=None, branchChildren=None):
        self.direction = direction
        self.growthChildren = growthChildren if growthChildren else []
        self.branchChildren = branchChildren if branchChildren else []

    def hasBranched(self):
        return not not self.branchChildren

    def hasGrown(self):
        return not not self.growthChildren

    def hasChildren(self):
        return self.hasBranched() or self.hasGrown()

    def getSymbol(self):
        return BranchNode.mapDirectionToSymbol[self.direction]

    def newBranch(self, branchNode):
        self.branchChildren.append(branchNode)

    def newGrowth(self, branchNode):
        self.growthChildren.append(branchNode)


class Branches:
    # Spawns one visible branch (either left or right) when init'd

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
        branchChildNode = BranchNode(random.choice((2, 4)))

        self.rootBranchNode = BranchNode(
            3, branchChildren=[branchChildNode])
        self.branchOriginDataDict = branchOriginDataDict

        self.growthProbability = .75

    def _recursiveAgingSearch(self, branchNode, grabBranchableCandidates, returnList):
        # If it's grown, it can't branch
        # If it's branched, it can't grow

        # Base Case
        if not branchNode.hasChildren():
            returnList.append(branchNode)
            return returnList

        # Recursive Case
        if grabBranchableCandidates:
            # find branchables, given they have children
            if branchNode.hasGrown():
                self._recursiveAgingSearch(
                    branchNode.growthChildren[0], grabBranchableCandidates, returnList)
                return returnList
            elif len(branchNode.branchChildren) < 2:
                returnList.append(branchNode)
                self._recursiveAgingSearch(
                    branchNode.branchChildren[0], grabBranchableCandidates, returnList)
                return returnList
            else:
                self._recursiveAgingSearch(
                    branchNode.branchChildren[0], grabBranchableCandidates, returnList)
                self._recursiveAgingSearch(
                    branchNode.branchChildren[1], grabBranchableCandidates, returnList)
                return returnList
        else:
            # find growables, given they have children
            if branchNode.hasBranched():
                for branchChild in branchNode.branchChildren:
                    self._recursiveAgingSearch(
                        branchChild, grabBranchableCandidates, returnList)
                return returnList
            else:
                returnList.append(branchNode)
                self._recursiveAgingSearch(
                    branchNode.growthChildren[0], grabBranchableCandidates, returnList)
                return returnList

    def _getAgingCandidates(self, grabBranchableCandidates):
        returnList = []
        self._recursiveAgingSearch(
            self.rootBranchNode, grabBranchableCandidates, returnList)
        return returnList

    def _getGrowableBranches(self):
        return self._getAgingCandidates(False)

    def _growChild(self):
        growableBranches = self._getGrowableBranches()
        branchNodeToGrow = random.choice(growableBranches)
        childDirection = branchNodeToGrow.direction
        branchNodeToGrow.newGrowth(BranchNode(childDirection))

    def _getBranchableBranches(self):
        return self._getAgingCandidates(True)

    def _branchChild(self):
        branchableBranches = self._getBranchableBranches()
        branchNodeToGrow = random.choice(branchableBranches)

        branchableDirections = Branches.mapDirectionToBranchDirections[branchNodeToGrow.direction]

        for branchChild in branchNodeToGrow.branchChildren:
            branchableDirections.remove(branchChild.direction)

        childDirection = random.choice(branchableDirections)
        branchNodeToGrow.newBranch(BranchNode(childDirection))

    def handleAging(self):
        # for now, grow a new segment every tick
        if random.random() < self.growthProbability:
            self._growChild()
        else:
            self._branchChild()

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
