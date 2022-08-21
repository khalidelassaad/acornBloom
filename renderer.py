import curses


def renderWorld(cursesScreen, worldArray):
    cursesScreen.refresh()

    height, width = cursesScreen.getmaxyx()
    pad = curses.newpad(height, width + 1)

    for y in range(height):
        for x in range(width):
            pad.addch(y,x, worldArray[y][x])

    pad.refresh(0, 0, 0, 0, height - 1, width - 1)

def renderInitialAcorn(cursesScreen):
    cursesScreen.refresh()


if __name__ == "__main__":
    pass