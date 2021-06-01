if __name__ == '__main__':
    print("Input:")
    print("Enter Size of Array : ")
    N=int(input())
    print("Enter Array elements seperated by spaces : ")
    A =list(map(int,input().strip().split()))[:N]
    print("Enter k value : ")
    k=int(input())
    count =0

hash_dict_val = dict()
hash_dict_count = dict()

for i in range(N) :
  hash_dict_val[A[i]] = 2*A[i]-k

for i in range(N):
  if A[i] not in hash_dict_count:
      hash_dict_count[A[i]] = 0
  hash_dict_count[A[i]] += 1

for i in range(N) :
  new_array = A[:i] + A[i+1:]
  if hash_dict_val[A[i]] in new_array and hash_dict_count[A[i]] > 1 :
    count += hash_dict_count[A[i]] - 1
  elif hash_dict_val[A[i]] in new_array :
    count += 1
count
