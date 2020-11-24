import random
#import time as time_


def millis():
    return int(round(time_.time() * 1000))


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = []
    greats = []
    equals = []
    less = [x for x in arr if x < pivot]
    greats = [x for x in arr if x > pivot]
    equals = [pivot] * arr.count(pivot)
    #for x in arr:
    #	if x < pivot:
    #		less.append(x)
    #	elif x > pivot:
    #		greats.append(x)
    #	else:
    #		equals.append(x)
    return quicksort(less) + equals + quicksort(greats)


def segments_count(arr):
    assert len(arr) > 0
    result = [0] * arr[len(arr) - 1]
    last = arr[0]
    count = 0
    for x in range(len(arr)):
    	if arr[x] != last:
    		result[last - 1] = count
    		count = 0
    		last = arr[x]
    	count += 1
    result[len(result) - 1] = count if arr[len(arr) - 1] == last else 1
    return result


def main():
	segments_count, points = map(int, input().split())
	segments = [[int(x) for x in input().split()] for _ in range(segments_count)]
	points = [int(x) for x in input().split()]
	arr = []
	for seg in segments:
		for x in range(seg[0], seg[1] + 1):
			arr.append(x)
	s = quicksort(arr)
	c = segments_count(s)
	print(c)
	res = [counted_arr[x] for x in points]
	print(*res)



    #arr_dimension = 1000
    #arr_range = 1000
    #loops = 1

    #start = millis()
    #for loop in range(loops):
        #arr = [random.randint(1, arr_range) for _ in range(arr_dimension)]
        #print(arr)
        #arr_sort = quicksort(arr)
        #print(arr_sort)
        #print("Время работы быстрой сортировки {} раз массива из {} чисел в диапазоне {} - {} мс".format(loops,
        #  arr_dimension, arr_range, millis() - start))
        #start = millis()
        #print(segments_count(arr_sort, arr_range))
        #print("Время подсчета количества каждого числа в массиве {} мс".format(millis() - start))
    


if __name__ == '__main__':
    main()
