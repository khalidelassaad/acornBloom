class Branch:
    def __init__(self, branchOriginDataDict):
        self.branchDict = {
            (0, 0): branchOriginDataDict,
            (0, 1): {"symbol": "K"}
        }

        # TODO: add a branch!

    def handleAging(self):
        pass

    def getBranchDict(self):
        return self.branchDict
