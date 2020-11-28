def max_steps_sum(steps_costs):
    dim = [[0 for _ in range(0, 2)] for _ in range (len(steps_costs) + 1)]
    dim[1][0] = steps_costs[0]
    for i in range(2, len(steps_costs) + 1):
        dim[i][0] = max(dim[i - 1][0], dim[i - 1][1]) + steps_costs[i - 1]
        dim[i][1] = dim[i - 1][0]
    return dim[len(dim) - 1][0]


def test():
    assert -63 == max_steps_sum([-2, -16, -13, -9, -48])
    assert 2 == max_steps_sum([1, 1, -2, -4, -6, 2, 2])
    assert 3 == max_steps_sum([1, 2])
    assert 1 == max_steps_sum([2, -1])
    assert 3 == max_steps_sum([-1, 2, 1])
    assert 2 == max_steps_sum([2])
    assert -2 == max_steps_sum([-2])


def main():
    _ = int(input())
    steps_costs = [*map(int, input().split())]
    print(max_steps_sum(steps_costs))


if __name__ == '__main__':
    main()
