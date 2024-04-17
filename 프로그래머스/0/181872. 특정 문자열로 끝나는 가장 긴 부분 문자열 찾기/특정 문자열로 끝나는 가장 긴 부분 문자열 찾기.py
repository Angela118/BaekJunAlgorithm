from collections import deque

def solution(myString, pat):
    myString = list(myString)
    
    que = deque()
    idx=0
    for i in range(len(myString)-1,-1,-1):
        if len(que) == len(pat):
            que.pop()        
        que.appendleft(myString[i])        
        if "".join(que) == pat:
            idx = i+len(pat)
            break
        
        
    return "".join(myString[:idx])