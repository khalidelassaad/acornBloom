import random

from tree.branch import Branch


class Trunk:

    trunkSymbols = ["|", "‖"]

    def __init__(self, originDataDict):
        self.trunkDict = {
            (0, 0): originDataDict
        }
        self.branchObjectsDict = dict()
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
            self.lengthenProbability += -0.1

    def getTrunkDict(self):
        trunkDict = self.trunkDict.copy()
        for branchCoords, branchObject in self.branchObjectsDict.items():
            for branchSegmentCoords, branchSegmentDataDict in branchObject.getBranchDict().items():
                trunkDictCoords = tuple(sum(x) for x in zip(
                    branchCoords, branchSegmentCoords))
                trunkDict[trunkDictCoords] = branchSegmentDataDict
        return trunkDict

    def _thicken(self):
        self.isThick = True
        for data in self.trunkDict.values():
            data["symbol"] = self._getTrunkChar()

    def _createNewBranchOriginAtCoords(self, coords):
        branchOriginDataDict = self.trunkDict[coords]

        # Transform branchOriginDataDict accordingly
        branchOriginDataDict["type"]["trunk"]["isBranchRoot"] = True

        # Instantiate branch object
        branchObject = Branch(branchOriginDataDict)

        # Save branch object in trunk dict at coords
        branchOriginDataDict["type"]["trunk"]["branchObject"] = branchObject

        # Save branch object in branches origins dict
        self.branchObjectsDict[coords] = branchObject

    def _beginBranching(self):
        branchNodeCoords = (-self.highestTrunk, 0)
        self._createNewBranchOriginAtCoords(branchNodeCoords)

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
