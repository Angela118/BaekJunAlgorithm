def solution(array, commands):
    answer = []
    
    temp=[]
    for n in range(len(commands)):
        i = commands[n][0]
        j = commands[n][1]
        k = commands[n][2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    
    print(answer)
    return answer