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


def main():
    arr_dimension = 100000
    arr_range = 100000
    loops = 10

    start = millis()
    for loop in range(loops):
        arr = [random.randint(1, arr_range) for _ in range(arr_dimension)]
        arr_sort = quicksort(arr)
    print("Время работы быстрой сортировки {} раз массива из {} чисел в диапазоне {} - {} мс".format(loops,
          arr_dimension, arr_range, millis() - start))


if __name__ == '__main__':
    main()
