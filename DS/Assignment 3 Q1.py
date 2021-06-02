if __name__ == '__main__':
    print("Input:")
    print("Enter Size of Array : ")
    N=int(input())
    print("Enter Array elements seperated by spaces : ")
    A =list(map(int,input().strip().split()))[:N]
    print("Enter k value : ")
    k=int(input())
    count =0

#Hash table to store the value 2*A[i]-k
hash_dict_val = dict()

# Hash table to store the count of element in array A
hash_dict_count = dict()

# Fill values in hash table with values 2*A[i]-k 
for i in range(N) :
  hash_dict_val[A[i]] = 2*A[i]-k

# Fill values in hash table with count of occurance of element in list A
for i in range(N):
  if A[i] not in hash_dict_count:
      hash_dict_count[A[i]] = 0
  hash_dict_count[A[i]] += 1

# Now find he number of instances for which the condition" 2*A[i] - A[j]  = k; such that i != j" is true.
for i in range(N) :
  new_array = A[:i] + A[i+1:]
  if hash_dict_val[A[i]] in new_array and hash_dict_count[A[i]] > 1 :
    count += hash_dict_count[A[i]] - 1
  elif hash_dict_val[A[i]] in new_array :
    count += hash_dict_count[hash_dict_val[A[i]]]



print("Output : ",count)
