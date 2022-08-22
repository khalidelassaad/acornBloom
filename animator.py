from renderer import drawTreeOnWorldArray, renderWorld
from time import sleep
from tree import Tree
from world import initializeWorld 


def startAnimationLoop(worldArray, cursesScreen):
    height, width = cursesScreen.getmaxyx()
    initializeWorld(worldArray)
    trees = [
        # Tree((height * 7) // 10, width // 2)
        Tree(2 , width // 2) # TODO: delete me!
    ]
    while True:
        for tree in trees:
            tree.ageOneYear()
            # if tree.age == 25:
            #     return
            drawTreeOnWorldArray(worldArray, tree, showAge=True)
        renderWorld(cursesScreen, worldArray)
        sleep(.01)
