from renderer import renderInitialAcorn, renderWorld
from time import sleep

def transformWorld(worldArray, i):
    worldArray[i][i] = " "

def startAnimation(worldArray, cursesScreen):
    for i in range(20):
        transformWorld(worldArray, i)
        renderWorld(cursesScreen, worldArray)
        sleep(.1)
    renderInitialAcorn(cursesScreen)