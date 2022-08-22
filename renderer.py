import curses

from tree import Tree


def renderWorld(cursesScreen, worldArray):
    cursesScreen.refresh()

    height, width = cursesScreen.getmaxyx()
    pad = curses.newpad(height, width + 1)

    for y in range(height):
        for x in range(width):
            pad.addch(y,x, worldArray[y][x])

    pad.refresh(0, 0, 0, 0, height - 1, width - 1)
    return pad

def drawTreeOnWorldArray(worldArray, tree: Tree):
    for coords, symbol in tree.getTreePieces():
        treeY, treeX = tree.getCoords()
        pieceY, pieceX = coords
        worldArray[treeY + pieceY][treeX + pieceX] = symbol

if __name__ == "__main__":
    pass