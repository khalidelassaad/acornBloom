from roots import Roots


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

    def getCoords(self):
        return (self.y, self.x)

    def ageOneYear(self):
        self.age += 1
        self.handleAging()
        return self.age

    def handleAging(self):
        if self.age % 1 == 0:
            self.growOneRootSegment()
            # TODO: call self.Roots.handleAging

    def getTreeDictItems(self):
        return self.treeDict.items()
