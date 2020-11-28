def diff(x, y):
    return 0 if x == y else 1


def search_edit_dist_line(first, second):
    n, m = len(first), len(second)
    dim = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        dim[i][0] = i
    for j in range(0, m + 1):
        dim[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = diff(first[i - 1], second[j - 1])
            dim[i][j] = min(dim[i - 1][j] + 1, dim[i][j - 1] + 1, dim[i - 1][j - 1] + c)
    return dim[n][m]


def search_edit_dist_reversed(first, second):
    dim = [[-1 for _ in range(0, len(first) + 1)] for _ in range(0, len(second) + 1)]
    i0, j0 = len(first) - 1, len(second) - 1

    def search(i, j):
        if dim[i][j] < 0:
            if i == 0:
                dim[i][j] = j
            elif j == 0:
                dim[i][j] = i
            else:
                ins = search(i, j - 1) + 1
                dlt = search(i - 1, j) + 1
                sub = search(i - 1, j - 1) + diff(first[i], second[j])
                dim[i][j] = min(ins, dlt, sub)
        return dim[i][j]

    return search(i0, j0)


def main():
    first = str(input())
    second = str(input())
    print(search_edit_dist_line(first, second))


if __name__ == '__main__':
    main()
