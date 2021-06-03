
def StackPushPopDelay(array_1, array_2, size):
    Stack = []
    Queue = []
    j = 0

    for i in range(0, size):
        if array_1[i] == array_2[j]:
            Stack.append(array_1[i])
            j = j + 1
        else:
            Queue.append(array_1[i])

    while j < size:
        tmp = Queue[0]
        if tmp == array_2[j]:
            Stack.append(tmp)
            Queue.remove(tmp)
            j = j + 1

        else:
            break

    if j == size:
        print("Yes")
    else:
        print("No")


# Main Code
if __name__ == '__main__':
    m = int(input())
    Input = list(map(int, input().strip().split()))[:m]
    Input.reverse()
    output = list(map(int, input().strip().split()))[:m]
    print(''.join(str(Input).split(',')))
    print(''.join(str(output).split(',')))

    StackPushPopDelay(Input, output, m)
    
