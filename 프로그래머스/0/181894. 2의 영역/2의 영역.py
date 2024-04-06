def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
            
    
    return arr[answer[0]:answer[-1]+1] if answer else [-1]