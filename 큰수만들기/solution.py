def solution(number, k):
    answer = []
    cnt = 0
    for n in number:
        while answer and answer[-1]<n and cnt<k:
            answer.pop()
            cnt+=1
        answer.append(n)
    # 제거가 덜 된 경우
    # 제거가 덜 된 갯수만큼 뒤에서 제거
    if cnt<k:
        answer = answer[:cnt-k]

    return "".join(answer)

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))