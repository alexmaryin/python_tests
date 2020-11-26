import random
import time


def get_rank_digit(number, length, rank):
	assert length >= rank
	digit = (number // (10**(length - rank))) % 10
	return digit


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


def radix_sort(arr):
	radix = 10
	max_len = False
	tmp, placement = -1, 1
	while not max_len:
		max_len = True
		buckets = [list() for _ in range(radix)]
		for i in arr:
			tmp = i / placement
			buckets[int(tmp % radix)].append(i)
			if max_len and tmp > 0:
				max_len = False
		a = 0
		for b in range(radix):
			buck = buckets[b]
			for i in buck:
				arr[a] = i
				a += 1
		placement *= radix
	return arr


def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = random.choice(arr)
	less = [x for x in arr if x < pivot]
	greats = [x for x in arr if x > pivot]
	equals = [pivot] * arr.count(pivot)
	return quicksort(less) + equals + quicksort(greats)


length = 100
numbers = 10
print('Генерация массива из {} числел разрядностью {}'.format(numbers, length))
arr = [random.randint(10**(length-1), 10**length - 1) for _ in range(numbers)]
print(arr)
start = time.time() * 1000
sorted_arr = rank_sort(arr, length)
end = time.time() * 1000
print('Затрачено на поразрядную сортировку {} мс (разряд вычисляется)'.format(end - start))
print(sorted_arr)
start = time.time() * 1000
sorted_arr = radix_sort(arr)
end = time.time() * 1000
print('Затрачено на поразрядную сортировку {} мс (разряд вычисляется, реализация чужая)'.format(end - start))
print(sorted_arr)
start = time.time() * 1000
sorted_Arr = quicksort(arr)
end = time.time() * 1000
print('Затрачено на быструю^3 сортировку {} мс'.format(end - start))
print(sorted_arr)