import random
from sys import stdin
from math import ceil


def lis_bottom_up(arr):
    temp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(0, i):
            #if arr[j] < arr[i]:						# для поиска строго возрастающей последовательности
            # if arr[i] % arr [j] == 0:				# для поиска наибольшей последовательнократной подпоследовательности
            if arr[j] >= arr[i]:		# для поиска наибольшей невозрастающей последовательности, т.е. 5 4 4 4 3 3 2 1 к примеру
                temp[i] = max(temp[i], temp[j] + 1)
    ans = max(temp)
    return ans


def lis_naive(arr):
	lens = [1] * len(arr)
	tops = [-1] * len(arr)
	for i in range(len(arr)):
		for j in range(0, i):
			if arr[j] >= arr[i] and lens[i] < lens[j] + 1:
				lens[i] = lens[j] + 1
				tops[i] = j
	ans_index = lens.index(max(lens))
	path = []
	path_indicies = []
	while ans_index >= 0:
		path.append(arr[ans_index])
		path_indicies.append(ans_index + 1)
		ans_index = tops[ans_index]
	path.reverse()
	path_indicies.reverse()
	return path, path_indicies


def lis_bisect(arr):
	n = len(arr)
	pred = [0] * n
	indicies = [0] * (n + 1)
	last = 0
	arr = arr[::-1]
	for i in range(n):
		lo, hi = 1, last
		while lo <= hi:
			mid = ceil((lo + hi) / 2)
			if arr[indicies[mid]] <= arr[i]:
				lo = mid + 1
			else:
				hi = mid - 1
		newlast = lo
		pred[i] = indicies[newlast - 1]
		if newlast > last:
			indicies[newlast] = i
			last = newlast
		elif arr[i] < arr[indicies[newlast]]:
			indicies[newlast] = i
	seq = [0] * last
	key = indicies[last]
	for i in range(last - 1, -1, -1):
		seq[i] = n - key
		key = pred[key]
	return seq


def main():
	#max_len = 20
	# inp = [random.randint(0, max_len ** 2) for _ in range(max_len)]
	#inp = [5, 3, 4, 4, 2]
	#print(inp)
	#max_len = int(input())
	#inp = [int(x) for x in input().split()]
	#print(lis_bottom_up(inp))
	# path, indicies = map(list, lis_naive(inp))
	max_len = (int(stdin.readline()))
	inp = [int(x) for x in stdin.readline().split()]
	indicies = lis_bisect(inp)
	print(len(indicies))
	print(' '.join(map(str, indicies[::-1])))


if __name__ == '__main__':
	main()
