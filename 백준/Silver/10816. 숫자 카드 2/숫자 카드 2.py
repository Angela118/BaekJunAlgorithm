import sys
from collections import Counter


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    card_list = map(int, sys.stdin.readline().split())
    M = int(sys.stdin.readline())
    target_list = map(int, sys.stdin.readline().split())
    ans=[]

    counts = Counter(card_list)

    print(" ".join([str(counts[target]) if target in counts else str(0) for target in target_list]))