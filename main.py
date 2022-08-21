import curses

from animator import startAnimation
from renderer import renderInitialAcorn, renderWorld
from utility import startKeyboardListeners
from time import sleep


def runSimulation(cursesScreen):
    renderWorld(cursesScreen)
    renderInitialAcorn(cursesScreen)

    while True:
        # cursesScreen.clear()
        cursesScreen.refresh()
        sleep(1)

    startKeyboardListeners()

    startAnimation()
    return

if __name__ == "__main__":
    curses.wrapper(runSimulation)