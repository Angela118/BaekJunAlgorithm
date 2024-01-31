import sys
from collections import defaultdict


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sg_nums = map(int, sys.stdin.readline().split())
    M = int(sys.stdin.readline())
    correct = map(int, sys.stdin.readline().split())
    ans=[]
    counts = defaultdict(int)
    for num in sg_nums:
        counts[num]+=1

    for num in correct:
        if num in counts:
            ans.append(str(counts[num]))
        else:
            ans.append(str(0))

    print(" ".join(ans))