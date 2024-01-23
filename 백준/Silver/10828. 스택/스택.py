import sys

def stack_func(stack_list, data):
    data = data.split()
    if data[0] == 'push':
        stack_list.append(data[1])
    elif data[0] == 'pop':
        if not stack_list:
            print(-1)
        else:
            print(stack_list[-1])
            stack_list.pop()
    elif data[0] == 'size':
        print(len(stack_list))
    elif data[0] == 'empty':
        if not stack_list:
            print(1)
        else:
            print(0)
    elif data[0] == 'top':
        if not stack_list:
            print(-1)
        else:
            print(stack_list[-1])



if __name__ == '__main__':
    iterator = int(sys.stdin.readline())
    stack_list=[]

    for _ in range(iterator):
        data = sys.stdin.readline()
        stack_func(stack_list, data)

