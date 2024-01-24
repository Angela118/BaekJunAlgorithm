import sys
from collections import deque


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())

    queue_list = deque(range(1, N+1))
    result=[]
    
    while queue_list:
        for _ in range(K-1):
            queue_list.append(queue_list.popleft())
        result.append(str(queue_list.popleft()))

    
    print("<", ", ".join(result), ">", sep='')