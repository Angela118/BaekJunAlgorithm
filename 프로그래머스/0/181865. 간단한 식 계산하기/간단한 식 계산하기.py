def solution(binomial):
    answer = binomial.split(" ")
    
    for i in range(len(answer)):
        if answer[i].isdigit():
            answer[i] = int(answer[i])
            
    if answer[1] == '+':
        answer[0]+=answer[2]
    elif answer[1] == '-':
        answer[0]-=answer[2]
    elif answer[1] == '*':
        answer[0]*=answer[2]
            
    return answer[0]