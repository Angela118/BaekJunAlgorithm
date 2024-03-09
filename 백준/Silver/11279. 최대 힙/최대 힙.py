import sys
import heapq

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    values=[]
    for _ in range(N):
        values.append(int(sys.stdin.readline()))

    heap=[]
    for val in values:
        if val==0:
            if not heap:
                print(0)
            else:
                print(-heapq.heappop(heap))
        else:
            heapq.heappush(heap,-val)
