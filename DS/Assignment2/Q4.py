def Next_Greatest(a, n):

	stack = []

	array = [0 for i in range(n)]
	for i in range(n-1, -1, -1):
		while (len(stack) > 0 and stack[-1] <= a[i]):
			stack.pop()
		if (len(stack) == 0):
			array[i] = -1		
		else:
			array[i] = stack[-1]	
		stack.append(a[i])
  
	return array


if __name__=='__main__':
  print ("Input")
  N = int(input("Enter Size of array : "))
  print("Enter Integers seperated by spaces ")
  A = list(map(int,input().strip().split()))[:N]
  array=Next_Greatest(A,len(A))
  print ("Output")
  print(*array, sep=' ')
