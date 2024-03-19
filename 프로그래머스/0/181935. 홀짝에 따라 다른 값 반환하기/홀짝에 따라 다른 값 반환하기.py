def solution(n):
    answer = 0
    if n%2!=0:
        for num in range(n+1):
            if num%2!=0:
                answer+=num
    else:
        for num in range(n+1):
            if num%2==0:
                answer+=num**2
                
    return answer