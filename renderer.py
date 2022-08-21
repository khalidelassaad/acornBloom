import curses

def renderWorld(cursesScreen):
    cursesScreen.refresh()
    pad = curses.newpad(24, 81)

    awoArbitraryWorldObject = [["o" for _ in range(80)] for _ in range(24)]

    for y in range(24):
        for x in range(80): # 
            pad.addch(y,x, awoArbitraryWorldObject[y][x])

    pad.refresh(0, 0, 0, 0, 23, 79)

def renderInitialAcorn(cursesScreen):
    pass

def awoObjectToString(awoArbitraryWorldObject):
    awoArbitraryWorldObject = [["o" for _ in range(80)] for _ in range(24)]
    awoString = ""
    for line in awoArbitraryWorldObject:
        for char in line:
            awoString += char
        awoString += "\n"
    return awoString

if __name__ == "__main__":
    awoString = awoObjectToString([["o" for _ in range(80)] for _ in range(24)])

    print("\n" + awoString)