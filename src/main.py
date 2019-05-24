import bin_search
from sys import argv


def main(d):
    min_v = bin_search.min_value(d)
    max_v = bin_search.max_value()
    print(bin_search.bin_search(min_v, max_v, d))


if len(argv) == 2:
    main(int(argv[1]))
else:
    print('Proper syntax: python3 main.py [d]')
