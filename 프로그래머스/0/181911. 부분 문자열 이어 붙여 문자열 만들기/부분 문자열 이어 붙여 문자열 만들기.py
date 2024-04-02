def solution(my_strings, parts):
    for i in range(len(my_strings)):
        my_strings[i] = list(my_strings[i])
        my_strings[i] = my_strings[i][parts[i][0]:parts[i][1]+1]
        my_strings[i] = "".join(my_strings[i])
        
    return "".join(my_strings)