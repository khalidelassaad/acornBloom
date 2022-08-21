from renderer import renderInitialAcorn, renderWorld
from time import sleep

def initializeWorld(worldArray):
    height = len(worldArray)
    width = len(worldArray[0])
    horizonLevel = (height * 3) // 5
    worldArray[horizonLevel] = ["-" for _ in range(width)]

def transformWorld(worldArray, i):
    worldArray[i][i] = "X"

def startAnimation(worldArray, cursesScreen):
    initializeWorld(worldArray)
    for i in range(20):
        transformWorld(worldArray, i)
        renderWorld(cursesScreen, worldArray)
        sleep(.1)
    renderInitialAcorn(cursesScreen)