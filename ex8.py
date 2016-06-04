from collections import namedtuple


def conversion_table(rate = 1):
	'''
	Generate currency conversion table between curr & euros with the given conversion rate (amount of euros for a single unit of curr).
	'''
	# structure to pair currency values
	Conversion = namedtuple('Conversion', ['foreign','euro'])
	# denominations
	denoms = [d * 10**e for e in range(6) for d in [1,2,5]]
	# euro denominations
	e_denoms = list(filter(lambda e: e <= 100, denoms))
	# (curr, euro) values for euro denoms
	from_euros = [Conversion(e * rate, e) for e in e_denoms]
	# (curr, euro) values for currency denoms
	curr_values = [Conversion(c, c * (1/rate)) for c in denoms]
	# weave lists
	return merge_lists(from_euros, curr_values)

def print_table(currency, table):
	'''
	Print conversion table to screen.
	'''
	print()
	for e in table:
		print('{:10.2f} {} = {:6.2f} EUR'.format(e.foreign, currency, e.euro))
	print()

def d_round(n):
	'''
	Round number to nearest magnitude of 10 relative to the size of n.
	Example: 3.14 -> 3, 15.34 -> 20, 442.234 -> 400.
	'''
	# round & convert to string
	x = str(round(n))
	# num of digits after first digit
	size = 10**(len(x)-1)
	# divide, round, multiply
	return round(int(x)/size)*size

def merge_lists(A, B):
	'''
	Merge the list B within the list A in ascending order. The resulting list starts & ends with the first & last elements of A. Ex. [a1, b1,...., bn, am]
	'''
	l = list()
	# element pairs from A
	pairs = zip(A[:-1], A[1:])
	# for each pair in A
	for x, y in pairs:
		# add first element
		l.append(x)
		# add successive B elements, up to next euro amount
		l += filter(lambda e: x.foreign < e.foreign <= y.foreign, B)
	# cap the end with last elem of A
	l.append(A[-1])
	return l


currency = input('Currency: ')
ex_rate = input('Exchange Rate (euros for foreign unit): ')
ex_rate= float(ex_rate)
inverse_rate = 1/ex_rate
table = conversion_table(inverse_rate)
print_table(currency, table)
