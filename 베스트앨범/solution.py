def solution(genres, plays):
    answer = []

    n = len(genres) # 장르 갯수
    dic = {} # 모든 노래를 장르별로 나누어 [고유번호, 플레이 횟수] 형태로 담은 딕셔너리

    for i in range(n):
        if genres[i] in dic:
            dic[genres[i]].append([i, plays[i]])
        else:
            dic[genres[i]] = [[i, plays[i]]]

    playSum = {} # 장르 별 플레이횟수 총합을 담을 딕셔너리
    for g in dic.keys():
        cnt = 0
        for value in dic[g]:
            cnt+=value[1]
        playSum[g] = cnt

    playSum = sorted(playSum.items(), key=lambda x:x[1], reverse = True) #플레이 횟수 총 합이 높은 순으로 장르 정렬
    
    for tmp in playSum:
        g = tmp[0]
        rank = sorted(dic[g], key = lambda x:x[1], reverse = True)
        
        answer.append(rank[0][0])
        if len(rank)>=2:
            answer.append(rank[1][0])
    
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
