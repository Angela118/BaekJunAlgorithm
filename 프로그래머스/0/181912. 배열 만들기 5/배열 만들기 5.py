def solution(intStrs, k, s, l):
    answer = []
    res=[]
    for i in range(len(intStrs)):
        intStrs[i] = list(intStrs[i])
        res.append(int("".join(intStrs[i][s:s+l])))
        if res[i]>k:
            answer.append(res[i])
        
    return answer