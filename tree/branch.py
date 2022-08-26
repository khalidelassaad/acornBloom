import random


class Branch:
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
