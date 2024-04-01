def solution(my_string, queries):
    my_string = list(my_string)
    
    for s, e in queries:
        if s==0:
            my_string[s:e+1] = my_string[e::-1]
        else:
            my_string[s:e+1] = my_string[e:s-1:-1]
            
    return "".join(my_string)