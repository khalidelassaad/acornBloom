def renderWorld(cursesScreen):

    awoArbitraryWorldObject = [["o" for _ in range(80)] for _ in range(24)]
    awoString = awoObjectToString(awoArbitraryWorldObject)

    cursesScreen.addstr(0, 0, awoString)
    pass

def renderInitialAcorn(cursesScreen):
    pass

def awoObjectToString(awoArbitraryWorldObject):
    awoArbitraryWorldObject = [["o" for _ in range(80)] for _ in range(24)]
    awoString = "" # Define me :)
    for line in awoArbitraryWorldObject:
        for char in line:
            awoString += char
        awoString += "\n"
    return awoString

if __name__ == "__main__":
    awoString = awoObjectToString([["o" for _ in range(80)] for _ in range(24)])

    print("\n" + awoString)