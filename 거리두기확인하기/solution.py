
#각 place가 거리두기를 지켰으면 1, 지키지 않았으면 0을 반환하는 함수
def check(p):
    
    #면접 대기자들의 위치(행,열)를 저장할 리스트
    applicant = []
    

    #모든 면접 대기자의 위치를 applicant 리스트에 저장 
    for row in range(5):
        for col in range(5):
            if p[row][col]=='P':
                applicant.append((row,col))

    #각 면접 대기자마다 다른 면접 대기자와의 거리를 확인
    for j in range(len(applicant)-1):
        for i in range(j,len(applicant)):
            #맨해튼 거리가 1
            if abs(applicant[j][0]-applicant[i][0])+abs(applicant[j][1]-applicant[i][1])==1:
                return 0
            #맨해튼 거리가 2
            elif abs(applicant[j][0]-applicant[i][0])+abs(applicant[j][1]-applicant[i][1])==2:

                #수직
                if applicant[j][0]==applicant[i][0] or applicant[j][1]==applicant[i][1]:
                    #둘 사이(중점)에 파티션이 아닌 빈자리 존재
                    if p[(applicant[j][0]+applicant[i][0])//2][(applicant[j][1]+applicant[i][1])//2]=="O":
                        return 0
                #대각선
                elif p[applicant[j][0]][applicant[i][1]]=="O" or p[applicant[i][0]][applicant[j][1]]=="O":
                    return 0
    return 1

        

    
            
    

def solution(places):
    answer = []

    #각 교실을 돌며 거리두기를 잘 지키고 있는지 여부를 확인하여 answer에 저장
    for p in places:
        answer.append(check(p))
    
    return answer
