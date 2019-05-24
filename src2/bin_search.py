import math
import geneticAlgorithm
import readFile
import afunction


def bin_search(a, b, d):
    print("bin: <", a, ", ", b, ">")
    point = math.floor((a + b) / 2)
    if a == b or a == b - 1:
        print("sensors: ", a)
        print()
        res = max_area_for(a, d, 150, 250)
        if res[0] >= 90:
            return a, res[1]  #second return - sensors' position
        else:
            return b, last_max_area_for(b, d, 150, 250)

    result = max_area_for(point, d, 150, 250)

    if result[0] >= 0.9:
        return bin_search(a, point, d)
    else:
        return bin_search(point, b, d)


def max_area_for(number, d, mi, lambd):
    return geneticAlgorithm.main_gen(mi, lambd, d, number)


def last_max_area_for(number, d, mi, lambd):
    return geneticAlgorithm.last_gen(mi, lambd, d, number)



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

