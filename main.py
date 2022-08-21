import curses

from animator import startAnimation
from renderer import renderInitialAcorn, renderWorld
from utility import startKeyboardListeners
from time import sleep


def runSimulation(cursesScreen):
    curses.curs_set(False)

    renderWorld(cursesScreen)
    renderInitialAcorn(cursesScreen)

    cursesScreen.refresh() # may not be necessary
    cursesScreen.getkey()

    startKeyboardListeners()

    startAnimation()
    return

if __name__ == "__main__":
    curses.wrapper(runSimulation)
