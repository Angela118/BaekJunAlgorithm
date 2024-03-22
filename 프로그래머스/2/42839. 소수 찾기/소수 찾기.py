from itertools import permutations

def isPrime(n):
    if n==1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
            else:
                return True

def solution(numbers):
    answer = []
    numbers = [n for n in numbers]  # numbers를 하나씩 자른다.
    
    # 모든 조합 찾기
    per_nums = []
    for i in range(1, len(numbers)+1):
        per_nums += list(permutations(numbers, i))    
    
    
    # 중복되지 않는 int형 리스트로 바꾸기
    per_list = ["".join(p) for p in per_nums]    
    per_list = list(set(map(int, per_list)))
    
    
    # for per in per_list:
    #     if isPrime(per):
    #         answer+=1
    
    for n in per_list:                            # 모든 int형 숫자에 대해 소수인지 판별
        if n < 2:                                 # 2보다 작은 1,0의 경우 소수 아님
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):        # n의 제곱근 보다 작은 숫자까지만 나눗셈
            if n % i == 0:                        # 하나라도 나눠떨어진다면 소수 아님!
                check = False
                break
        if check:
            answer.append(n)                      # 소수일경우 answer 배열에 추가

    return len(set(answer))  
    
    # return answer