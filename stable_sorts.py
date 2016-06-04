
def bubblesort(A, f = lambda x, y: x > y):
	# end index of unsorted part
	end = len(A) - 1
	# while still unsorted
	while end > 0:
		last_change = 0
		# for each elem in unsorted
		for i in range(end):
			# if out of order
			if f(A[i], A[i+1]):
				# swap
				A[i], A[i+1] = A[i+1], A[i]
				# note index
				last_change = i
		# update new end index
		end = last_change

from random import randint

nums = [randint(0,3) for _ in range(5)]
A = list(zip("abcde", nums))
B = A[:]

print()
print('Unsorted list:\t\t', A,'\n')
bubblesort(B, lambda x, y: x[1] > y[1])
print('Bubblesort (stable):\t', B,'\n')
bubblesort(B, lambda x, y: x[1] >= y[1])
print('Bubblesort (unstable):\t', B,'\n')
