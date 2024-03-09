import sys
from math import *
import heapq

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    heap=[]
    for _ in range(N):
        val = int(sys.stdin.readline())

        if val==0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (abs(val), val))
