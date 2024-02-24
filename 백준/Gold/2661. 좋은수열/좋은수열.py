import sys


def back_tracking(idx):
    # 나쁜 순열인지 체크
    # 현재까지 ans에 저장된 순열을 절반으로 나눠서 인접한 곳에 중복된 순열이 있는지 확인
    for i in range(1, (idx//2)+1):  
        if ans[-i:] == ans[-2*i:-i]:    # 뒤에서부터 확인한다.
            return -1   # 중복인 경우, pop() 해주기 위해 함수에서 빠져나감


    if idx == N:    # N개가 다 찼을 경우
        for i in range(N):
            print(ans[i], end="")
        
        return 0    # 완성!!


    for i in range(1, 4):   # 작은 수를 찾아야 하기 때문에 1,2,3 순서대로 넣는다.
        ans.append(i)
        if back_tracking(idx+1) == 0:
            return 0
        ans.pop()



if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ans=[]

    back_tracking(0)

