def solution(arr, queries):
    answer = []
    
    for j in range(len(queries)):
        temp=[]
        for i in arr[queries[j][0]:queries[j][1]+1]:
            if (i > queries[j][2]):
                temp.append(i)
        
        if not temp:
            answer.append(-1)
        else:
            answer.append(min(temp))
            
    
    return answer