def knapsack_reps_BU(weight, items, costs):
    acc = [0] * weight
    for i in range(len(acc)):
        for j in range(len(items)):
            if items[j] <= i:
                acc[i] = max(acc[i], acc[i - items[j]] + costs[j])
    return acc[weight - 1]


def knapsack_noreps_BU(weight, items, costs):
    acc = [[0 for _ in range(weight + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for w in range(0, weight + 1):
            acc[i][w] = acc[i - 1][w]
            if items[i - 1] <= w:
                acc[i][w] = max(acc[i][w], acc[i - 1][w - items[i - 1]] + costs[i - 1])
    return acc[len(items)][weight]


def main():
    weight, count = map(int, input().split())
    costs = [w for w in map(int, input().split())]
    items = costs
    assert len(costs) == len(items)
    # weight = 10
    # items = [6, 3, 4, 2]
    # costs = [30, 16, 14, 9]
    # print(knapsack_reps_BU(weight, items, costs))
    print(knapsack_noreps_BU(weight, items, costs))


if __name__ == '__main__':
    main()
