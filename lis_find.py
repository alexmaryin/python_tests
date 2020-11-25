def lis_bottom_up(arr):
    temp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                temp[i] = max(temp[i], temp[j] + 1)
    ans = max(temp)
    return ans


def main():
    inp = [1, 5, 3, 3, 5, 7, 8, 4, 9, 3, 3, 10]
    print(lis_bottom_up(inp))


if __name__ == '__main__':
    main()
