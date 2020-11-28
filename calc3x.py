def calculate_naive(number):
    res, k, n = [], 0, number
    if number == 1:
        return 0, [1]
    while n > 0:
        if n % 3 == 0:
            x = int(n / 3)
            res.append(n)
            n -= x
            k += 1
        elif n % 2 == 0:
            x = int(n / 2)
            res.append(n)
            n -= x
            k += 1
        else:
            res.append(n)
            n -= 1
            k += 1
    return k, res


def calculate(number):
    if number == 1:
        return 0, [1]
    steps = [0] * (number + 1)
    prevs = [0] * (number + 1)
    for i in range(1, number):
        a, b, c = i * 2, i * 3, i + 1
        if a <= number:
            if steps[a] == 0 or steps[i] + 1 < steps[a]:
                steps[a] = steps[i] + 1
                prevs[a] = i
        if b <= number:
            if steps[b] == 0 or steps[i] + 1 < steps[b]:
                steps[b] = steps[i] + 1
                prevs[b] = i
        if c <= number:
            if steps[c] == 0 or steps[i] + 1 < steps[c]:
                steps[c] = steps[i] + 1
                prevs[c] = i
    factors = [number]
    last = prevs[number]
    while steps[last] > 0:
        factors.append(last)
        last = prevs[last]
    factors.append(1)
    factors.reverse()
    return steps[number], factors


def main():
    number = int(input())
    ops, factors = calculate(number)
    print(ops)
    print(*factors)


if __name__ == '__main__':
    main()
