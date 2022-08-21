import curses

from animator import startAnimation
from renderer import renderInitialAcorn, renderWorld
from utility import startKeyboardListeners


def runSimulation(cursesScreen):
    height, width = cursesScreen.getmaxyx()
    curses.curs_set(False)

    worldArray = [["o" for _ in range(width)] for _ in range(height)]
    renderWorld(cursesScreen, worldArray)
    renderInitialAcorn(cursesScreen)

    cursesScreen.refresh() # may not be necessary
    cursesScreen.getkey()

    startKeyboardListeners()

    startAnimation()
    return

if __name__ == "__main__":
    curses.wrapper(runSimulation)
