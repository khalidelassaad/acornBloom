import curses

from tree.tree import Tree


def renderWorld(cursesScreen, worldArray):
    cursesScreen.refresh()

    height, width = cursesScreen.getmaxyx()
    pad = curses.newpad(height, width + 1)

    for y in range(height):
        for x in range(width):
            pad.addch(y, x, worldArray[y][x])

    pad.refresh(0, 0, 0, 0, height - 1, width - 1)
    return pad


def drawTreeOnWorldArray(worldArray, tree: Tree, showAge=False):
    worldArrayCopy = []
    for row in worldArray:
        worldArrayCopy.append(row.copy())

    treeY, treeX = tree.getCoords()
    for coords, data in tree.getTreeDictItems():
        symbol = data["symbol"]
        pieceY, pieceX = coords
        try:
            worldArrayCopy[treeY + pieceY][treeX + pieceX] = symbol
        except IndexError:
            pass

    charSpace = 2
    for char in str(tree.age):
        worldArrayCopy[treeY][treeX + charSpace] = char
        charSpace += 1

    return worldArrayCopy


if __name__ == "__main__":
    pass
