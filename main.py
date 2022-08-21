

from animator import startAnimation
from display import openCursesWindow
from renderer import renderInitialAcorn, renderWorld
from utility import startKeyboardListeners

def runSimulation():
    openCursesWindow()
    renderWorld()
    renderInitialAcorn()
    startKeyboardListeners()

    startAnimation()
    return

if __name__ == "__main__":
    runSimulation()