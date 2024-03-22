from itertools import permutations


def solution(numbers):
    numbers = [n for n in numbers]  # numbers를 하나씩 자른다.
    
    # 모든 조합 찾기
    per_nums = []
    for i in range(1, len(numbers)+1):
        per_nums += list(permutations(numbers, i))    
    
    
    # 중복되지 않는 int형 리스트로 바꾸기
    per_list = [int("".join(p)) for p in per_nums]    
    per_list = list(set(per_list))
    print(per_list)
    
    answer=0
    for per in per_list:
        if per<2:
            continue
        
        flag=True
        for i in range(2, int(per**0.5)+1):
            if per%i == 0:
                flag=False
                break
                
        if flag:
            answer+=1
            
    
    return answer