
# Reference : https://www.geeksforgeeks.org/stack-permutations-check-if-an-array-is-stack-permutation-of-other/

from queue import Queue
def StackPermutation(stack1, op, n):
  input_ = Queue()
  output_ = Queue()
  for i in range(n):
    input_.put(stack1[i])
    output_.put(op[i])

  stack2 = []
  while(not input_.empty()):
    element = input_.queue[0]
    input_.get()
    if (element == output_.queue[0]):
      output_.get()
      while(len(stack2) != 0):
        if(stack2[-1]==output_.queue[0]):
          stack2.pop()
          output_.get()
        else:
          break
    else:
      stack2.append(element)

  if (len(stack2) == 0 and input_.empty()):
    print('Yes')
  else:
    print('No')


if __name__ == '__main__':
    print("Please Enter the initial stack elements seperated by spaces:")
    stack1 = list(map(int,input().strip().split(' ')))
    
    print("Please Enter the final order elements seperated by spaces:")
    
    op = list(map(int,input().strip().split(' ')))
    print(*stack1, sep = ' ')
    print(*op, sep = ' ')
    
    StackPermutation(stack1, op, len(stack1))
