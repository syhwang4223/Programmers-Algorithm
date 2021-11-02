def solution(s):

    length = len(s)
    if length==1:
        return 1
    
    sol = []    #압축한 결과물들의 길이를 담는 리스트
    
    for i in range(1, length//2+1):
        #i개 단위로 압축
        word = s[0:i]   #압축해서 비교하는 단위
        cnt = 1
        comp = ''  #압축한 결과물
        
        for j in range(i,length,i):
            if s[j:j+i] == word:
                cnt+=1
            else:
                if cnt==1:
                    comp += word
                else:
                    comp += str(cnt) + word

                word = s[j:j+i]
                cnt = 1
                
        if cnt!= 1: #마지막 부분을 추가해주기 전에 반복문을 나오기 때문
            comp += str(cnt) + word
        else :
            comp += word

        sol.append(len(comp))

    return min(sol)
