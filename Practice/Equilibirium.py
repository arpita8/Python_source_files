"""def solution(l):
	total = sum(l)
	for i in range(len(l)):
		total -=l[i]


		if	total == sum:
			return i
		total += l[i]
	return -1	"""
def solution(A):
    left_sum = 0
    right_sum = sum(A)
    for i in range(len(A)):
        right_sum -= A[i]
        if left_sum == right_sum:
            return i
        left_sum += A[i]
    return -1

A = [-1,0,2,-3]
print(solution(A))