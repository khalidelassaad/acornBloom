import random


class BranchNode:
    def __init__(self, direction, children):
        self.direction = direction
        self.children = children
        self.hasBranched = False


class Branches:
    # DIRECTIONS:
    #     2 3 4
    #      \|/
    #    1 -+- 5
    #      / \
    #     0   6

    mapGrowthDirectionToCoordDelta = {
        0: (1, -1),
        1: (0, -1),
        2: (-1, -1),
        3: (-1, 0),
        4: (-1, 1),
        5: (0, 1),
        6: (1, 1)
    }

    mapDirectionToSymbol = {
        0: "/",
        1: "-",
        2: "\\",
        3: "|",
        4: "/",
        5: "-",
        6: "\\"
    }

    mapDirectionToBranchDirections = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4, 6],
        6: [5]
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
        leftBranchNode = BranchNode(2, None)
        rightBranchNode = BranchNode(4, None)
        self.rootBranchNode = BranchNode(3, [leftBranchNode, rightBranchNode])

    def handleAging(self):
        pass

    def getBranchDict(self):
        return self.branchDict
