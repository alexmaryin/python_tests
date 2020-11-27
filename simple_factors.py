from math import sqrt
from random import randint


def get_simple_factors(value):
	factors = []
	while value % 2 == 0:
		factors.append(2)
		value /= 2
	i = 3
	max_factor = round(sqrt(value))
	while i <= max_factor:
		if value % i == 0:
			factors.append(int(i))
			value /= i
			max_factor = round(sqrt(value))
		i += 2
	if value > 1:
		factors.append(int(value))
	return factors


simples = []
while len(simples) <= 100:
	x = randint(1, 10**6)
	if len(get_simple_factors(x)) < 2:
		simples.append(x)
print(simples)
