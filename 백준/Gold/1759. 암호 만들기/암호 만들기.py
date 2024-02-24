import sys

def check_vowcon(key_ans):
    vowels, consonants = 0, 0   # 모음, 자음 갯수 초기화

    for i in range(L):
        if key_ans[i] in vowels_list:
            vowels+=1
        else:
            consonants+=1

    if vowels>=1 and consonants>=2:
        return True
    else:
        return False
    

def back_tracking(idx):
    if len(key_ans) == L:  # L개의 알파벳으로 암호 생성시
        if check_vowcon(key_ans) == False:  # 모음, 자음 갯수 확인
            return
        
        print("".join(key_ans))
        return
    
    # 암호 만들기
    for i in range(idx, C):
        key_ans.append(C_list[i])
        back_tracking(i+1)
        key_ans.pop()


if __name__ == '__main__':
    L, C = map(int, sys.stdin.readline().split()) 
    C_list = sorted(list(map(str, sys.stdin.readline().split())))
    vowels_list = ['a','e','i','o','u']
    key_ans=[]
    back_tracking(0)


