def solution(arr, queries):
    arr2 = arr[:]
    
    for s, e, k in queries:
        for i in range(s, e+1):
            if i%k==0:
                arr2[i]+=1
    
    return arr2