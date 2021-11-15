def solution(numbers, target):    
    global answer
    answer = 0

    
    def dfs(index, summation):
        global answer
        
        #numbers를 조합하여 target 넘버를 완성한 경우
        if index==len(numbers)-1 and summation==target:
            answer+=1
            return
        
        # 타겟넘버는 못만들었지만 최대깊이까지 탐색한 경우
        elif index==len(numbers)-1:
            return
        
        # 깊이+1 탐색
        dfs(index+1, summation+numbers[index+1])
        dfs(index+1, summation-numbers[index+1])
   
    dfs(0,numbers[0])
    dfs(0,-numbers[0])
    
    return answer

print(solution([1,2,3],6))
