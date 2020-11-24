import random
from collections import Counter
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


def main():
	count, points = map(int, input().split())
	segments = [[int(x) for x in input().split()] for _ in range(count)]
	points = {int(x) for x in input().split()}
	arr = []
	for seg in segments:
		for x in range(seg[0], seg[1] + 1):
			arr.append(x)
	s = quicksort(arr)
	print(s)
	c = Counter(s)
	print(c)
	res = [c[x] for x in points]
	print(*res)


if __name__ == '__main__':
    main()
