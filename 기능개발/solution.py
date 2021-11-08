def solution(progresses, speeds):
    answer = []
    period = []

    for i in range(len(progresses)):
        period.append((100-progresses[i])//speeds[i])
        if (100-progresses[i])%speeds[i]!=0:
            period[i]+=1

    print(period)
    tmp = period[0]
    del period[0]
    cnt=1
 
    for i in range(len(period)):

        if period[i]<=tmp:
            cnt+=1
        else:
            answer.append(cnt)
            tmp = period[i]
            i+=cnt   
            cnt=1
        
    answer.append(cnt)
    return answer


#print(solution([93,30,55],[1,30,5]))
#print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
print(solution([9,9,9],[1,1,1]))
