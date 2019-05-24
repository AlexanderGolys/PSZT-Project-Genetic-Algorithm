def getArray(path = './config/data.txt'):
    with open(path) as file:
        array = [line.rstrip('\n') for line in file]
        convertedArray = []
    for i in range(len(array)):
        convertedArray.append(convertToInt(array[i]))
    return convertedArray


def getArrayTests(path = './config/data.txt'):
    with open(path) as file:
        array = [line.rstrip('\n') for line in file]
        convertedArray = []
    for i in range(len(array)):
        convertedArray.append(convertToFloat(array[i]))
    return convertedArray


def convertToInt(array):
    convertedArray = []
    for i in range(len(array)):
        convertedArray.append(int(array[i]))
    return convertedArray


def convertToFloat(array):
    convertedArray = []
    for i in range(len(array)):
        convertedArray.append(round(float(array[i]), 4))
    return convertedArray
