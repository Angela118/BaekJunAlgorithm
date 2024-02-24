import sys

def back_sum(idx, sum_n):
    global count

    if idx>=N:  # 인덱스가 N 보다 큰 경우, 리턴
        return

    sum_n += N_list[idx]    # 일단 현재 원소를 더한다.

    if sum_n == S:
        count+=1

    back_sum(idx+1, sum_n)  # 현재 원소를 선택한 경우
    back_sum(idx+1, sum_n-N_list[idx])  #현재 원소를 선택하지 않은 경우
    

if __name__ == '__main__':
    N, S = map(int, sys.stdin.readline().split()) 
    N_list = list(map(int, sys.stdin.readline().split()))
    count=0
    
    back_sum(0, 0)

    print(count)