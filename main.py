import curses

from animator import startAnimation
from renderer import renderInitialAcorn, renderWorld
from utility import startKeyboardListeners

def runSimulation(cursesScreen):
    renderWorld(cursesScreen)
    renderInitialAcorn(cursesScreen)
    startKeyboardListeners()

    startAnimation()
    return

if __name__ == "__main__":
    curses.wrapper(runSimulation)