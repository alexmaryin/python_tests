import random
import bisect


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
	segL = []
	segR = []
	for x in range(count):
		left, right = map(int, input().split())
		segL.append(left)
		segR.append(right)
	points = [int(x) for x in input().split()]
	segL = quicksort(segL)
	segR = quicksort(segR)
	results = []
	for x in points:
		left = bisect.bisect(segL, x) + 1
		right = bisect.bisect(segR, x) + 1
		results.append(left - right)
	print(*results)


if __name__ == '__main__':
    main()
