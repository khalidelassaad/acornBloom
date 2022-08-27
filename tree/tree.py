from tree.roots import Roots
from tree.trunk import Trunk


class Tree:
    agesDict = {}  # define tree stages and age milestones here

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.age = 0
        self.originDataDict = {
            "type": {
                "origin": None,
                "root": {
                    "incomingDirection": 3,
                    "outgoingBranches": 0
                }
            },
            "symbol": "@"
        }
        self.rootsObject = Roots(self.originDataDict)
        self.trunkObject = Trunk(self.originDataDict)

    def getCoords(self):
        return (self.y, self.x)

    def ageOneYear(self):
        self.age += 1
        self.handleAging()
        return self.age

    def handleAging(self):
        # TODO: age different components differently
        if self.age % 3 == 0:
            self.rootsObject.handleAging()
        if self.age % 1 == 0:
            self.trunkObject.handleAging(self.age)

    def getTreeDictItems(self):
        treeDict = dict()
        treeDict.update(self.rootsObject.getRootDict())
        treeDict.update(self.trunkObject.getTrunkDict())
        return treeDict.items()
