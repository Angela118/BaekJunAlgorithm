import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        parenthesis_string = sys.stdin.readline()
        stack_count=0

        for i in parenthesis_string:
            if i == '(':
                stack_count+=1
            elif i == ')':
                stack_count-=1
                if stack_count<0:
                    break

        if stack_count == 0:
            print('YES')
        else:
            print('NO')

    

    
