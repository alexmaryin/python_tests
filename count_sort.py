def count_sort(arr, count):
    dest = [0] * count
    for j in arr:
        dest[j - 1] += 1
    for i in range(2, count + 1):
        dest[i - 1] += dest[i - 2]
    result = [0] * len(arr)
    for j in range(len(arr) - 1, -1, -1):
        result[dest[arr[j] - 1] - 1] = arr[j]
        dest[arr[j] - 1] -= 1
    return result


def main():
    count = int(input())
    arr = [int(x) for x in input().split()]
    assert len(arr) == count
    res = count_sort(arr, 10)
    print(*res)


if __name__ == '__main__':
    main()
