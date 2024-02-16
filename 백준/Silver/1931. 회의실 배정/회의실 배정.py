import sys
    

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    durations = []

    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        durations.append([start, end])


    # durations[i][j]에서 i에 대해 먼저 오름차순 정렬 후, j에 대해 오름차순 정렬
    durations.sort(key=lambda x:(x[1], x[0]))
    
    # 어차피 가장 첫 원소가 제일 먼저 끝나는 회의이기 때문에 for문 밖에서 처리 후 삭제
    num_meet=1
    meeting = durations[0]
    del durations[0]

    for start, end in durations:
        if meeting[1] <= start:
            num_meet+=1
            meeting = [start, end]


    print(num_meet)