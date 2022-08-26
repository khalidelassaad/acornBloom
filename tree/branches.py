import random


class Branches:
    # DIRECTIONS:
    #     2 3 4
    #      \|/
    #    1 -+- 5
    #      / \
    #     0   6

    mapDirectionStepToCoordDelta = {
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

    def __init__(self, branchOriginDataDict):
        firstBranch = random.choice([((0, 1), "/"), ((0, -1), "\\")])

        self.branchDict = {
            (0, 0): branchOriginDataDict,
            firstBranch[0]: {"symbol": firstBranch[1]}
        }

        # TODO: add a branch!

    def handleAging(self):
        pass

    def getBranchDict(self):
        return self.branchDict
