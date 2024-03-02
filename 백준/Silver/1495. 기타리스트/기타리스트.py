import sys


if __name__ == '__main__':
    N, S, M = map(int, sys.stdin.readline().split())
    V = list(map(int, sys.stdin.readline().split()))

    # (N+1) x (M+1) 배열로, 각 곡 마다 가능한 볼륨을 1로 담기
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][S] = 1

    for i in range(N):
        for j in range(M+1):
            if dp[i][j]==1: # i번재 곡에 담겨있는 볼륨
                # 다음 곡에서 가능한 볼륨
                plus = j + V[i]     # 다음 곡에서 V[i] 만큼 볼륨을 증가 시킨 경우
                minus = j - V[i]    # 다음 곡에서 V[i] 만큼 볼륨을 감소 시킨 경우

                if 0<= plus <=M:    # 증가 시킨 볼륨이 가능 범위 내에 있는 경우, 다음 곡에 볼륨 담기
                    dp[i+1][plus]=1
                if 0<= minus <=M:   # 감소 시킨 볼륨이 가능 범위 내에 있는 경우, 다음 곡에 볼륨 담기
                    dp[i+1][minus]=1

    
    answer=-1
    for i in range(M, -1, -1):
        if dp[N][i]==1:
            answer=i
            break

    print(answer)