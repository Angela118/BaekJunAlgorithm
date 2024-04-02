def solution(my_string):
    len_my = len(my_string)
    answer = []
    
    my_string = list(my_string)
    for i in range(len_my):
        answer.append(my_string[i:])
        answer[i] = "".join(answer[i])
        
    return sorted(answer)