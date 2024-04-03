def solution(my_string, is_prefix):
    my_string = list(my_string)
    answer=[]
    for i in range(len(my_string)):
        answer.append(my_string[:len(my_string)-i])
        answer[i] = "".join(answer[i])
        
    return 1 if is_prefix in answer else 0