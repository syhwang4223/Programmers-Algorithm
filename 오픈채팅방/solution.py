def solution(record):
    answer = []
    member = {}
    result = []
    
    for statements in record:
        s = tuple(statements.split())
        if s[0] == "Change":
           member[s[1]] = s[2]
        elif s[0] == "Enter":
            member[s[1]] = s[2]
            answer.append((True, s[1]))
        else:
            answer.append((False, s[1]))

           
    #출력
    for enter, uid in answer:
        message = member[uid] + "님이 "
        if enter:
            message += "들어왔습니다."
        else:
            message += "나갔습니다."
        result.append(message)                          
          
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
