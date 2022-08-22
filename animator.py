from renderer import drawTreeOnWorldArray, renderWorld
from time import sleep
from tree import Tree
from world import initializeWorld 


def startAnimationLoop(worldArray, cursesScreen):
    height, width = cursesScreen.getmaxyx()
    initializeWorld(worldArray)
    trees = [
        Tree((height * 7) // 10, width // 2)
    ]
    while True:
        for tree in trees:
            tree.ageOneYear()
            drawTreeOnWorldArray(worldArray, tree)
        renderWorld(cursesScreen, worldArray)
        sleep(.1)
