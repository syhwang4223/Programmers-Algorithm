def solution(n, lost, reserve):
    #도난당했지만 여벌도 가지고 있는 학생들 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    return n-len(lost_set)

    return answer


print(solution(5, [2,4],[1,3,5]))
