import sys



# def dfs(x, y, visited, total_prob):
    


if __name__ == '__main__':
    N = int(sys.stdin.readline())

    T, P=[0], [0]
    for _ in range(N):
        t, p = map(int, sys.stdin.readline().split())
        T.append(t)
        P.append(p)

    profit = [0 for _ in range(N+1)]
    
    for now in range(1, N+1):
        profit[now] = max(profit[now-1], profit[now])    # 현재까지의 최대 이익을 이전까지의 최대 이익으로 갱신
        finish_date = now + T[now] - 1  # 이번 상담의 끝나는 날짜 (당일 포함)
        if finish_date <= N:  # 이번 상담이 퇴사일 전에 끝나는 경우 (이번 상담을 실시하는 경우)
            # 이번 상담이 끝나는 날의 이익 = max(이전까지의 최대 이익+이번 상담으로 얻을 수 있는 이익, 끝나는 날짜의 최대 이익)
            profit[finish_date] = max(profit[now-1]+P[now], profit[finish_date])
        


    print(profit[-1])