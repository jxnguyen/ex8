
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

def mergesort(A, f = lambda x,y: x <= y):

	def merge(X, Y):
		result = []
		# while elements in both lists
		while X and Y:
			result.append(X.pop(0) if f(X[0],Y[0]) else Y.pop(0))
		# consume remaining elems
		return result + (X if X else Y)

	# base case
	if len(A) <= 1: return A

	# split lists & merge
	mid   = len(A)//2
	left  = mergesort(A[:mid],f)
	right = mergesort(A[mid:],f)
	return merge(left, right)

# TEST SUITE
# ==============================================
from random import randint

nums = [randint(0,3) for _ in range(5)]
A = list(zip("abcde", nums))
B = A[:]

# BUBBLE SORT
# ----------------------------------------------
print()
print('Unsorted list:\t\t', A,'\n')
bubblesort(B, lambda x, y: x[1] > y[1])
print('Bubblesort (stable):\t', B,'\n')
B = A[:]
bubblesort(B, lambda x, y: x[1] >= y[1])
print('Bubblesort (unstable):\t', B,'\n')

# MERGE SORT
# ----------------------------------------------
B = A[:]
B = mergesort(B, lambda x,y: x[1] <= y[1])
print('Mergesort (stable):\t', B,'\n')
B = A[:]
B = mergesort(B, lambda x,y: x[1] < y[1])
print('Mergesort (unstable):\t', B,'\n')
