def initializeWorld(worldArray):
    height = len(worldArray)
    width = len(worldArray[0])
    horizonLevel = (height * 3) // 5
    worldArray[horizonLevel] = ["-" for _ in range(width)]
