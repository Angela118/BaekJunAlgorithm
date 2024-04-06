def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if answer and answer[-1] == arr[i]:
            answer.pop()
        answer.append(arr[i])
    
    
    return answer