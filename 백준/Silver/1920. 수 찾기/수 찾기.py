import sys

def find_num(N_nums, target):
    start, end = 0, len(N_nums)-1
    while start <= end:
        mid = (start+end)//2

        if N_nums[mid] == target:
            return 1
        elif N_nums[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    N_nums = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    M_nums = list(map(int, sys.stdin.readline().split()))

    N_nums.sort()
    
    for num in M_nums:
        print(find_num(N_nums, num))