def initializeWorld(worldArray):
    height = len(worldArray)
    width = len(worldArray[0])
    horizonLevel = (height * 3) // 5
    worldArray[horizonLevel] = ["-" for _ in range(width)]

def transformWorld(worldArray, i):
    worldArray[i][i] = "X"