# here im making a change

def conversion_table(rate = 1):
	'''
	Generate currency conversion table between curr & euros with the given conversion rate (amount of euros for a single unit of curr).
	'''
	# euro denominations
	e_denoms = [1, 2, 5, 10, 20, 50, 100]
	# (euro, curr) values for euro denoms
	from_euros = [(e, e * rate) for e in e_denoms]
	# currency denominations
	c_denoms = gen_c_denoms(from_euros)
	# (euro, curr) values for currency denoms (with inverse rate)
	from_curr = [(c * (1/rate), c) for c in c_denoms]
	# weave lists
	return weave_lists(from_euros, from_curr)

def print_table(currency, table):
	'''
	Print conversion table to screen.
	'''
	print()
	for euro, curr in table:
		print('{:10.2f} {} = {:6.2f} EUR'.format(curr, currency, euro))
	print()

def gen_c_denoms(info):
	'''
	Returns a list of appropriate denominations of currency with respect to the Euro denominations.
	'''
	# retrieve conversion amounts for each euro denom
	_, amounts = zip(*info)
	# calculate midpoints between amounts & round
	return [d_round(a * 1.5) for a in amounts[:-1]]

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

def weave_lists(A, B):
	'''
	Return the list produced by alternating elements from A and B. Alternation
	starts with A and ends when either list is exhausted. Any remaining elements
	are concatenated afterwards.
	Example: [a,b,c,d,e] & [1,2,3] -> [a,1,b,2,c,3,d,e]
	'''
	l = list()
	i = 0
	# while i not overbounds
	while i < len(A) and i < len(B):
		# alternate appends
		l.append(A[i])
		l.append(B[i])
		i += 1

	# concatenate remaing elements if any
	if i < len(A): l += A[i:]
	if i < len(B): l += B[i:]
	return l





currency = input('Currency: ')
ex_rate = input('Exchange Rate (euros for foreign unit): ')
ex_rate= float(ex_rate)
inverse_rate = 1/ex_rate
table = conversion_table(inverse_rate)
print_table(currency, table)
