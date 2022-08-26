import random


class Trunk:

    def __init__(self, originDataDict):
        self.trunkDict = {
            (0, 0): originDataDict
        }
        self.thickeningThreshold = random.choice(range(3, 6))
        self.branchingThreshold = random.choice(range(2, 4))
        self.lengthenProbability = 1

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
        pass

    def _beginBranching(self):
        pass

    def _lengthen(self):
        pass
