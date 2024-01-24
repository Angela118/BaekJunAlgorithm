import sys

def parenthesis_stack(parenthesis_string):
    stack_list=[]

    for i in range(len(parenthesis_string)):
        if parenthesis_string[i] == '(':
            stack_list.append(parenthesis_string[i])
        elif parenthesis_string[i] == ')':
            if not stack_list:
                return 'NO'
            else:
                stack_list.pop()
        

    if not stack_list:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        parenthesis_string = sys.stdin.readline()
        result = parenthesis_stack(parenthesis_string)
        print(result)
