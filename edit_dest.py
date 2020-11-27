def search_edit_dist(first, second):
    dim = [[-1 for _ in range(0, len(first) + 1)] for _ in range(0, len(second) + 1)]
    i0, j0 = len(first) - 1, len(second) - 1

    def diff(x, y):
        return 0 if x == y else 1

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
    a = search_edit_dist('editing', 'emitting')
    print(a)


if __name__ == '__main__':
    main()
