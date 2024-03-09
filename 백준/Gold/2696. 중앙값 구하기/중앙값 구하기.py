import sys
import heapq


def heap_mid(values):
    leftheap=[]     # max heap
    rightheap=[]    # min heap
    mid = values[0]
    ans = [values[0]]

    for i in range(1, M):   # 입력받은 값의 1번 인덱스 값부터 불러온다. 그리고 idx는 1 부터 시작
        if values[i] > mid:   # 입력받은 val이 현재의 중간값 보다 큰 경우
            heapq.heappush(rightheap, values[i])  # 오른쪽 힙(min heap)에 넣어준다.
        else:
            heapq.heappush(leftheap, -values[i])  # 왼쪽 힙(max heap)
            
        if i % 2 == 0:    # values에서의 홀수번째 입력인 경우
            if len(leftheap) < len(rightheap):  # 왼쪽 힙이 오른쪽 힙 보다 길이가 짧을 경우,
                heapq.heappush(leftheap, -mid)  # 이전의 mid값을 왼쪽 힙에 넣어주고
                mid = heapq.heappop(rightheap)  # 오른쪽 힙에서 가장 작은 수를 꺼내서 mid값을 갱신한다.
            elif len(leftheap) > len(rightheap):
                heapq.heappush(rightheap, mid)
                mid = -heapq.heappop(leftheap)
            
            ans.append(mid)
    
    print(len(ans))

    for i in range(len(ans)):
        if (i > 0) and (i % 10 == 0):   # 정답값이 0보다 크고, 10으로 나누어 떨어질 때
            print()                     # 줄 바꾸기
        print(ans[i], end=' ')  
    print()




if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        M = int(sys.stdin.readline())
        
        values=[]
        if M % 10 == 0:     # 입력이 10개 단위로 들어오는거 처리
            for _ in range(M//10):
                values.extend(list(map(int, sys.stdin.readline().split())))
        else:
            for _ in range(M//10 + 1):
                values.extend(list(map(int, sys.stdin.readline().split())))

        
        heap_mid(values)
