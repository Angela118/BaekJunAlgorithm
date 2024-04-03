def solution(my_string, m, c):
    my_string = list(my_string)
    len_string = len(my_string)
    res=[[0] for _ in range(len_string//m)]
    
    for i in range(len_string):
        res[i//m].append(my_string[i])
    
    answer = ''
    for i in range(len(res)):
        answer+=res[i][c]
    
    return answer