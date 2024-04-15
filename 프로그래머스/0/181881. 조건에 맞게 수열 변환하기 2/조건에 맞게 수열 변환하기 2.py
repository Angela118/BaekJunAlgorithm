def solution(arr):
    old = arr[:]
    j=0
    while 1:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i]%2==0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i]%2!=0:
                arr[i] = arr[i]*2 + 1
        
        if old == arr:
            return j
        else:
            old = arr[:]
            
        j+=1
      