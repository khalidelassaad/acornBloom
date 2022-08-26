import random

from tree.branch import Branch


class Trunk:

    trunkSymbols = ["|", "‖"]

    def __init__(self, originDataDict):
        self.trunkDict = {
            (0, 0): originDataDict
        }
        self.branchObjectsList = []
        self.thickeningThreshold = random.choice(range(3, 6))
        self.branchingThreshold = random.choice(range(8, 9))
        self.lengthenProbability = 1
        self.insertTrunkSegmentAtBottomProbability = 1
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
        for trunkCoords, trunkSegmentData in self.trunkDict.items():
            if trunkSegmentData["type"].get("trunk"):
                if trunkSegmentData["type"]["trunk"]["isBranchRoot"]:
                    branchCoords = trunkCoords
                    branchObject = trunkSegmentData["type"]["trunk"]["branchObject"]
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
        self.branchObjectsList.append(branchObject)

    def _beginBranching(self):
        branchNodeCoords = (-self.highestTrunk, 0)
        self._createNewBranchOriginAtCoords(branchNodeCoords)

    def _lengthen(self):
        self.highestTrunk += 1
        DEBUGinsertAtBottom = random.random(
        ) < self.insertTrunkSegmentAtBottomProbability and self.highestTrunk > 3
        if DEBUGinsertAtBottom:
            newTrunkCoords = (-1, 0)
            for i in range(self.highestTrunk, 1, -1):
                # Shift trunkDict "up 1", all except (0,0)
                # Get trunkDict items, sort based on height coord (highest first),
                # walk through and waterfall reassign until (-1, 0)
                currentCoords = (-i, 0)
                belowCoords = (-(i-1), 0)
                self.trunkDict[currentCoords] = self.trunkDict[belowCoords]
        else:
            newTrunkCoords = (-self.highestTrunk, 0)

        self.trunkDict[newTrunkCoords] = {
            "type": {
                "trunk": {
                    "isBranchRoot": False
                }
            },
            # TODO: remove all occurrences of debug var
            "symbol": [self._getTrunkChar(), "%"][DEBUGinsertAtBottom]
        }

    def _getTrunkChar(self):
        return Trunk.trunkSymbols[self.isThick]
