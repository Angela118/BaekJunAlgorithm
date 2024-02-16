import sys
    

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    P = sorted(list(map(int, sys.stdin.readline().split())))
    
    ans=0

    for i in range(len(P)):
        ans += (P[i]*(len(P)-i))

    
    print(ans)