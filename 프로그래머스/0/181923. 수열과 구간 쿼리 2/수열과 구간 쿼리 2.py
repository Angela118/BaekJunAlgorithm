def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        temp=[]
        for i in arr[s:e+1]:
            if (i > k):
                temp.append(i)
        
        if not temp:
            answer.append(-1)
        else:
            answer.append(min(temp))
            
    
    return answer