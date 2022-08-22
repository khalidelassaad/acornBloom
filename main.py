import curses

from animator import startAnimationLoop
from utility import startKeyboardListeners


def runSimulation(cursesScreen):
    height, width = cursesScreen.getmaxyx()
    curses.curs_set(False)

    worldArray = [[" " for _ in range(width)] for _ in range(height)]

    startKeyboardListeners()
    startAnimationLoop(worldArray, cursesScreen)
    cursesScreen.getkey()
    return

if __name__ == "__main__":
    curses.wrapper(runSimulation)
