import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    N = [int(sys.stdin.readline()) for _ in range(T)]

    dp = [1]*10001  # 1만 사용해서 합을 만든 경우로 초기화

    # 1과 2를 사용해서 합을 만든 경우
    for i in range(2, 10001):
        dp[i] += i//2

    for i in range(3, 10001):
        dp[i] += dp[i-3]

    for n in N:
        print(dp[n])
