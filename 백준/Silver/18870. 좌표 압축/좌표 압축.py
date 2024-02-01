import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    input_num = list(map(int, sys.stdin.readline().split()))
    sorted_num = sorted(list(set(input_num)))
    index_list = str(range(len(sorted_num)))

    sorted_dict = {}
    ans=[]

    for i, num in enumerate(sorted_num):
        sorted_dict[num] = i

    for num in input_num:
        ans.append(str(sorted_dict[num]))
    
    print(" ".join(ans))