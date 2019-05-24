import math
import readFile


def decode(genotype):
    gen = str(genotype)
    x = []
    y = []
    alpha = []
    x_len = math.ceil(math.log2(n()))
    y_len = math.ceil(math.log2(m()))
    no_sensors = len(gen)//(x_len + y_len + 2)
    for i in range(no_sensors):
        x_in_gray = int(gen[:x_len])
        x_in_binary = gray_to_binary(x_in_gray)
        x.append(int(str(x_in_binary), 2))
        gen = gen[x_len:]
        y_in_gray = int(gen[:y_len])
        y_in_binary = gray_to_binary(y_in_gray)
        y.append(int(str(y_in_binary), 2))
        gen = gen[y_len:]
        alpha.append(int(gen[:2], 2))
        gen = gen[2:]

    for i in range(len(x)):
        x[i] = scale(x[i], n())

    for i in range(len(y)):
        y[i] = scale(y[i], m())

    return x, y, alpha


def scale(rez, mm):
    return math.floor((mm * rez) / (2 ** math.ceil(math.log2(mm))))
  

def m():
    table = readFile.getArray()
    return len(table)


def n():
    table = readFile.getArray()
    return len(table[0])


def gray_to_binary(n):
    n = int(str(n), 2)  # convert to int

    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask

    return bin(n)[2:]



def m():
    table = readFile.getArray()
    return len(table)


def n():
    table = readFile.getArray()
    return len(table[0])
