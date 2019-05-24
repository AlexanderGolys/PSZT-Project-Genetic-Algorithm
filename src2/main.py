import bin_search
from sys import argv


def main(d):
    min_v = bin_search.min_value(d)
    max_v = bin_search.max_value()
    result = bin_search.bin_search(min_v, max_v, d) #number of sensors and their positions
    print("area: ", result[1][0])
    print("x: ", result[1][1][0])
    print("y: ", result[1][1][1])
    print("alpha: ", result[1][1][2])


    positions = result[1][1][0:3] #[0] - x, [1] - y, [2] - alpha
    tab = result[1][1][3]
    number = result[0]

    print(number, " - number of sensors")

    for i in range(number):
        if positions[2][i] == 0:
            tab[positions[1][i]][positions[0][i]] = '^'
        if positions[2][i] == 1:
            tab[positions[1][i]][positions[0][i]] = '<'
        if positions[2][i] == 2:
            tab[positions[1][i]][positions[0][i]] = 'v'
        if positions[2][i] == 3:
            tab[positions[1][i]][positions[0][i]] = '>'


    for i in range(len(tab)):
        for j in range(len(tab[0])):
            print(tab[i][j], " ", end='')
        print()

if len(argv) == 2:
    main(int(argv[1]))
else:
    print('Proper syntax: python3 main.py [d]')


main(2)
