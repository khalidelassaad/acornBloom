import curses

from animator import startAnimation
from utility import startKeyboardListeners
from time import sleep


def runSimulation(cursesScreen):
    height, width = cursesScreen.getmaxyx()
    curses.curs_set(False)

    worldArray = [["o" for _ in range(width)] for _ in range(height)]

    startKeyboardListeners()
    startAnimation(worldArray, cursesScreen)
    cursesScreen.getkey()
    return

if __name__ == "__main__":
    curses.wrapper(runSimulation)
