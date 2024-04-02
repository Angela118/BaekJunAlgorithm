def solution(my_string, is_suffix):
    my_string = list(my_string)
    my_list=[]
    for i in range(len(my_string)):
        my_list.append(my_string[i:])
        my_list[i] = "".join(my_list[i])
    
    return 1 if is_suffix in my_list else 0