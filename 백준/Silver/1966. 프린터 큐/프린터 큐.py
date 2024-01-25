import sys
from collections import deque

if __name__ == '__main__':
    testcase = int(sys.stdin.readline())

    for _ in range(testcase):
        N, M = map(int, sys.stdin.readline().split())
        doc_priority = deque(map(int, sys.stdin.readline().split()))
        idx = deque(range(len(doc_priority)))
        
        turn=0
        while doc_priority:
            if doc_priority[0] == max(doc_priority):
                turn+=1
                if idx[0] == M:
                    print(turn)
                    break
                else:
                    doc_priority.popleft()
                    idx.popleft()
            else:
                doc_priority.rotate(-1)
                idx.rotate(-1)
