def solution(my_string, indices):
    my_string= list(my_string)
    answer = ''
    for i in range(len(my_string)):
        if i in indices:
            continue
        answer+=my_string[i]
        
    return answer