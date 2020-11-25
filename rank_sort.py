import random
import time


def get_rank_digit_str(number, length, rank):
	num_as_str = str(number)
	assert len(num_as_str) >= rank
	return int(num_as_str[rank - 1])


def get_rank_digit(number, length, rank):
	assert length >= rank
	digit = (number // (10**(length - rank))) % 10
	return digit


def rank_sort_str(arr, length):
	tarr = arr
	for i in range(length, 0, -1):
		ranks = [0] * 10
		for j in tarr:
			ranks[get_rank_digit_str(j, length, i)] += 1
		for j in range(1, 10):
			ranks[j] += ranks[j - 1]
		res = [0] * len(tarr)
		for j in range(len(tarr) - 1, -1, -1):
			res[ranks[get_rank_digit_str(tarr[j], length, i)] - 1] = tarr[j]
			ranks[get_rank_digit_str(tarr[j], length, i)] -= 1
		tarr = res
	return res


def rank_sort(arr, length):
	tarr = arr
	for i in range(length, 0, -1):
		ranks = [0] * 10
		for j in tarr:
			ranks[get_rank_digit(j, length, i)] += 1
		for j in range(1, 10):
			ranks[j] += ranks[j - 1]
		res = [0] * len(tarr)
		for j in range(len(tarr) - 1, -1, -1):
			res[ranks[get_rank_digit(tarr[j], length, i)] - 1] = tarr[j]
			ranks[get_rank_digit(tarr[j], length, i)] -= 1
		tarr = res
	return res


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    greats = [x for x in arr if x > pivot]
    equals = [pivot] * arr.count(pivot)
    return quicksort(less) + equals + quicksort(greats)


length = 100
numbers = 10000
print('Генерация массива из {} числел разрядностью {}'.format(numbers, length))
arr = [random.randint(10**(length-1), 10**length - 1) for _ in range(numbers)]
start = time.time() * 1000
sorted_arr = rank_sort(arr, length)
end = time.time() * 1000
print('Затрачено на поразрядную сортировку {} мс (разряд вычисляется)'.format(end - start))
start = time.time() * 1000
sorted_arr = rank_sort_str(arr, length)
end = time.time() * 1000
print('Затрачено на поразрядную сортировку {} мс (разряд из строки)'.format(end - start))
start = time.time() * 1000
sorted_Arr = quicksort(arr)
end = time.time() * 1000
print('Затрачено на быструю^3 сортировку {} мс'.format(end - start))