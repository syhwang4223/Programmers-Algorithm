


    

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    #방문 여부 확인하는 배열
    check = [[False for i in range(m)] for j in range(n)]
    check[0][0]= True

    #bfs용 큐
    s=[]
    s.append((0,0,1)) #row,col,distance

    while s:
        current = s.pop(0)
        row = current[0]
        col = current[1]
        dist = current[2]
        
        print(row,col,dist)

        #상대팀 진영 도착
        if row==n-1 and col==m-1:
            return dist
    
        nextRow = [row+1,row-1,row,row]
        nextCol = [col,col,col-1,col+1]
        
        for i in range(4):
            if nextRow[i]<0 or nextRow[i]>=n or nextCol[i]<0 or nextCol[i]>=m:
                continue
            elif check[nextRow[i]][nextCol[i]]==False and maps[nextRow[i]][nextCol[i]]==1:
                check[nextRow[i]][nextCol[i]] = True
                s.append((nextRow[i],nextCol[i],dist+1))

        #print(s)
    
    return -1


#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1]]))
#print(solution([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
#print(solution([[1,1,1],[1,1,1],[1,1,1]]))

print(type((0,0,0)))

#큐를 사용할 때는 list말고 dequeue를 사용하는게 효울이 좋음!
#그리고 방문요소 체크를 pop할 때 말고 큐에 집어 넣을때 해야 함
#check 배열을 만들지 않고 푸는 방법



