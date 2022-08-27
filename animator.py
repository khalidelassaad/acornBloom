from renderer import drawTreeOnWorldArray, renderWorld
from time import sleep
from tree.tree import Tree
from world import addHorizonToWorldArray


def startAnimationLoop(worldArray, cursesScreen):
    height, width = cursesScreen.getmaxyx()
    addHorizonToWorldArray(worldArray)
    trees = [
        Tree((height * 3) // 5, width // 2)
    ]
    while True:
        for tree in trees:
            tree.ageOneYear()
            worldArrayWithTree = drawTreeOnWorldArray(
                worldArray, tree, showAge=True)
        renderWorld(cursesScreen, worldArrayWithTree)
        # sleep(.01)
