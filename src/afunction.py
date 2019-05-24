import readFile
import dekoder

# 0 - wolne
# 1 - sciana
# 2 - nie podlega monitorowaniu
# 3 - zasloniete
# 4 - policzone


def J(x, y, alpha, dep):
    table = readFile.getArray()
    no_0 = seen_counter_for_0(table)

    n = dekoder.n()  # szerokosc x
    m = dekoder.m()  # szerokosc y
    is_forbidden = False

    for k in range(len(x)):

        # print(alpha[k])
        # print(m)

        table = angel_change(alpha[k], table)
        temp_x = x[k]
        x[k] = change_x(alpha[k], x[k], y[k], n, m)
        y[k] = change_y(alpha[k], temp_x, y[k], n, m)

        # print(x[k])
        # print(y[k])

        temp = j_for_one(x[k], y[k], dep, table)
        table = temp[0]
        if temp[1]:
            is_forbidden = True
        table = angel_change_back(alpha[k], table)
        # print_matrix(table)

    if is_forbidden:
        return 0.6 * round((seen_counter(table) / no_0), 4)
    else:
        return round((seen_counter(table) / no_0), 4)


def J_return_forbidden(x, y, alpha, dep):
    table = readFile.getArray()
    no_0 = seen_counter_for_0(table)

    n = dekoder.n()  # szerokosc x
    m = dekoder.m()  # szerokosc y
    is_forbidden = False

    for k in range(len(x)):

        # print(alpha[k])
        # print(m)

        table = angel_change(alpha[k], table)
        temp_x = x[k]
        x[k] = change_x(alpha[k], x[k], y[k], n, m)
        y[k] = change_y(alpha[k], temp_x, y[k], n, m)

        # print(x[k])
        # print(y[k])

        temp = j_for_one(x[k], y[k], dep, table)
        table = temp[0]
        if temp[1]:
            is_forbidden = True
        table = angel_change_back(alpha[k], table)
        # print_matrix(table)

    if is_forbidden:
        return None
    else:
        return round((seen_counter(table) / no_0), 4)


def j_for_one(x, y, d, matrix=readFile.getArray()):
    d += 1
    n = len(matrix[0])  # szerokosc x
    m = len(matrix)  # szerokosc y

    blocked_ranges = []
    if_forbidden = False

    if matrix[y][x] == 1 or matrix[y][x] == 2:
        if_forbidden = True

    for i in range(d):

        if y-i < 0 or y-i >= m:
            break
        for ii in range(2*i + 1):
            if 0 <= x-i+ii < n and matrix[y - i][x - i + ii] == 0:
                if not if_in_ranges(blocked_ranges, get_coords(2*i + 1, ii)):
                    matrix[y-i][x-i+ii] = 4
                else:
                    matrix[y - i][x - i + ii] = 0

            elif 0 <= x-i+ii < n and matrix[y - i][x - i + ii] == 1:
                blocked_ranges = add_range(blocked_ranges, get_coords((2*i + 1), ii))

    return matrix, if_forbidden


def add_range(ranges, new):
    ranges.append(new)
    merge_ranges(ranges)
    return ranges


def merge_ranges(ranges):
    for i in ranges:
        for ii in ranges:
            if i[1] >= ii[0] and ii[1] >= i[0]:
                i[0] = min(i[0], ii[0])
                i[1] = max(i[1], ii[1])
                ii[0] = i[0]
                ii[1] = i[1]


def get_coords(length, index):
    return [index/length, (index+1)/length]


def if_in_ranges(ranges, coords):
    for i in ranges:
        if i[0] <= coords[0] <= i[1] and i[0] <= coords[1] <= i[1]:
            return True
    return False


def print_matrix(matrix1):
    for i in matrix1:
        print(str(i))
    print('')


def seen_counter(matrix2):
    nb = 0
    for i in matrix2:
        for ii in i:
            if ii == 4:
                nb += 1
    return nb


def seen_counter_for_0(matrix2):
    nb = 0
    for i in matrix2:
        for ii in i:
            if ii == 0:
                nb += 1
    return nb


def matrix_transpose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez


def matrix_vertical_symmetry(m):
    for i in m:
        i.reverse()
    return m


def matrix_horizontal_symmetry(m):
    rez = []
    for i in m:
        rez.insert(0, i)
    return rez


def angel_change(alpha, m):
    if alpha == 1:
        m = matrix_transpose(m)
        m = matrix_vertical_symmetry(m)
    elif alpha == 2:
        m = matrix_horizontal_symmetry(m)
    elif alpha == 3:
        m = matrix_vertical_symmetry(m)
        m = matrix_transpose(m)
    return m


def angel_change_back(alpha, m):
    if alpha == 1:
        m = angel_change(3, m)
    elif alpha == 2:
        m = angel_change(2, m)
    elif alpha == 3:
        m = angel_change(1, m)
    return m


def change_x(alpha, x, y, len_x, len_y):
    if alpha == 1:
        return len_y - y - 1
    elif alpha == 3:
        return y
    else:
        return x


def change_y(alpha, x, y, len_x, len_y):
    if alpha == 1:                      
        return x
    elif alpha == 2:                    
        return len_y - y - 1
    elif alpha == 3:                    
        return len_x - x - 1
    else:                               
        return y

#
# matrix22 = readFile.getArray()
#
# # print_matrix(matrix_vertical_symmetry(matrix22))
# # print_matrix(matrix_horizontal_symmetry(matrix22))
# # print_matrix(angel_change_back(0, matrix22))
#
#
# print(J(matrix22, [2, 6], [7, 6], [0, 1], 3))
