def binary(start,end,times,n):
    global answer
    
    if start>end:
        return
    mid = (start+end)//2 #검사하는데 걸리는 총 시간
    people = 0 #검사 완료한 사람 수
    for time in times:
        #각 심사관마다 처리할 수 있는 사람 수
        people+= mid//time
    if people>=n:#mid의 시간동안 n보다 많은 사람을 심사할 수 있으면
        answer=mid
        binary(start,mid-1,times,n)
    else:
        binary(mid+1,end,times,n)
        
    

def solution(n, times):
    global answer
    answer = 0
    
    times.sort()
    high = n*times[-1] #가장 오래 걸린는 경우의 총 시간
    
    binary(1,high,times,n)
    return(answer)


def solution2(n, times):
    answer=0
    
    left = 1
    right = n*max(times)

    while (left<=right):
        mid = (left+right)//2
        people = 0
        for time in times:
            people+= mid//time

        if people>=n:
            answer=mid
            right=mid-1
        else:
            left=mid+1

    return answer
