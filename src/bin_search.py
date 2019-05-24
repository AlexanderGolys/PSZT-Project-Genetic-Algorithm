import math
import geneticAlgorithm
import readFile
import afunction


def bin_search(a, b, d):
    print("bin: <", a, ", ", b, ">")
    point = math.floor((a + b) / 2)
    if a == b or a == b - 1:
        if max_area_for(a, d) >= 90:
            return a
        else:
            return b

    result = max_area_for(point, d)

    if result >= 0.9:
        return bin_search(a, point, d)

    elif result < 0.9:
        return bin_search(point, b, d)


def max_area_for(number, d):
    return geneticAlgorithm.main_gen(50, 150, d, number)


def min_value(d):
    max_area_per_sensor = 0
    for i in range(d + 1):
        max_area_per_sensor += 2 * i + 1
    table = readFile.getArray()
    n = len(table[0])
    m = len(table)
    area = 0.9 * m * n
    return math.floor(area / max_area_per_sensor)


def max_value():
    table = readFile.getArray()
    return afunction.seen_counter_for_0(table)

