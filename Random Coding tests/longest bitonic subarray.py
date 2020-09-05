arr=[2,6,8,5]
arr2=[1,5,5,2,6]
arr3=[1,1]
def largest_distance(A):
	I = [1] * len(A)
	for i in range(1, len(A)):
		if A[i - 1] >= A[i]:
			I[i] = I[i - 1] + 1
	D = [1] * len(A)
	for i in reversed(range(len(A) - 1)):
		if A[i] <= A[i + 1]:
			D[i] = D[i + 1] + 1
	lbs_len = 1
	beg = end = 0
	for i in range(len(A)):
		if lbs_len < I[i] + D[i] - 2:
			lbs_len = (I[i] + D[i] - 2)
	return lbs_len 
  
print(largest_distance(arr))
print(largest_distance(arr2))
print(largest_distance(arr3))