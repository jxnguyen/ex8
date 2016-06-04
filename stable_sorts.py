
def bubblesort(A):
	# end index of unsorted part
	end = len(A) - 1
	# while still unsorted
	while end > 0:
		last_change = 0
		# for each elem in unsorted
		for i in range(end):
			# if out of order
			if A[i] > A[i+1]:
				# swap
				A[i], A[i+1] = A[i+1], A[i]
				# note index
				last_change = i
		# update new end index
		end = last_change
