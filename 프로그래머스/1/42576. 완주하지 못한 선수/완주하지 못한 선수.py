def solution(participant, completion):
    dict_p={}
    for p in participant:
        if p not in dict_p:
            dict_p[p]=1
        else:
            dict_p[p]+=1
    
    for c in completion:
        if dict_p[c] != 0:
            dict_p[c]-=1
    
    for key in dict_p.keys():
        if dict_p[key] == 1:
            return key
    
    answer = ''
    return answer