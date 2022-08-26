import random


class Trunk:

    trunkSymbols = ["|", "‖"]

    def __init__(self, originDataDict):
        self.trunkDict = {
            (0, 0): originDataDict
        }
        self.thickeningThreshold = random.choice(range(3, 6))
        self.branchingThreshold = random.choice(range(2, 4))
        self.lengthenProbability = 1
        self.isThick = False
        self.highestTrunk = 0

    def handleAging(self, treeAge):
        # called by Tree.handleAging
        if treeAge == self.thickeningThreshold:
            self._thicken()
        if treeAge == self.branchingThreshold:
            self._beginBranching()
        if random.random() < self.lengthenProbability:
            self._lengthen()

    def getTrunkDict(self):
        return self.trunkDict

    def _thicken(self):
        self.isThick = True
        for data in self.trunkDict.values():
            data["symbol"] = self._getTrunkChar()

    def _beginBranching(self):
        pass

    def _lengthen(self):
        self.highestTrunk += 1
        newTrunkCoords = (-self.highestTrunk, 0)
        self.trunkDict[newTrunkCoords] = {
            "type": {
                "trunk": {
                    "isBranchRoot": False
                }
            },
            "symbol": self._getTrunkChar()
        }

    def _getTrunkChar(self):
        return Trunk.trunkSymbols[self.isThick]
