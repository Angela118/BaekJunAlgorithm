def solution(numbers, target):
    leaves = [0]    # 모든 계산 결과를 담을 리스트
    
    for num in numbers:
        temp=[]
        
        for leaf in leaves:
            temp.append(leaf+num)   # 더하는 경우
            temp.append(leaf-num)   # 빼는 경우
        
        leaves=temp
    
    # 모든 경우의 수(leaves)에 target 값이 있으면 +1
    answer = 0
    for i in leaves:
        if i==target:
            answer+=1
        
        
    return answer