import random
import time as time_


def millis():
    return int(round(time_.time() * 1000))


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    greats = [x for x in arr if x > pivot]
    equals = [pivot] * arr.count(pivot)
    return quicksort(less) + equals + quicksort(greats)


def segments_count(arr, dim):
    assert len(arr) > 0
    result = [0] * dim
    last = arr[0]
    count = 0
    for x in arr:
        if x != last:
            result[last - 1] = count
            last = x
            count = 0
        count += 1
    return result


def main():
    arr_dimension = 100
    arr_range = 10
    loops = 1

    start = millis()
    for loop in range(loops):
        arr = [random.randint(1, arr_range) for _ in range(arr_dimension)]
        print(arr)
        arr_sort = quicksort(arr)
        print(arr_sort)
        print(segments_count(arr_sort, arr_range))
    print("Время работы быстрой сортировки {} раз массива из {} чисел в диапазоне {} - {} мс".format(loops,
          arr_dimension, arr_range, millis() - start))


if __name__ == '__main__':
    main()
