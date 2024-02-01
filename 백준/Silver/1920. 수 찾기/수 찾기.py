import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    N_nums = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    M_nums = list(map(int, sys.stdin.readline().split()))

    for num in M_nums:
        if num in N_nums:
            print(1)
        else:
            print(0)