def solution(priorities, location):
    answer = 0

    while priorities:
        print(priorities)
        if priorities[0] < max(priorities):
            priorities.append(priorities[0])
            priorities.pop(0)
            location-=1
            if location==-1: location=len(priorities)-1
            
        else:
            priorities.pop(0)
            answer+=1
            location-=1
            if location==-1:break
            
    return answer


print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))
