import sys
    

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    coins=[]
    
    for _ in range(N):
        coin_input = int(sys.stdin.readline())
        coins.append(coin_input)

    
    coins.sort(reverse=True)
    count_coin=0
    for coin in coins:
        if K == 0:
            break

        if coin > K:
            continue
        else:
            count_coin+=(K//coin)
            K %= coin
            

    print(count_coin)