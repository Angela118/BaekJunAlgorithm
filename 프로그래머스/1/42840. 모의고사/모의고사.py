def solution(answers):
    answer = [0,0,0]
    ans1, ans2, ans3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == ans1[i%5]:
            answer[0]+=1
        
        if answers[i] == ans2[i%8]:
            answer[1]+=1
        
        if answers[i] == ans3[i%10]:
            answer[2]+=1
        
    res=[]
    for i in range(len(answer)):
        if answer[i] == max(answer):
            res.append(i+1)
            
    
    return res