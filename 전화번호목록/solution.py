##def solution(phone_book):
##    answer = True
##    l = len(phone_book)
##
##    #phone_book.sort()
##    for i in range(l):
##        l2 = len(phone_book[i])
##        for j in range(l):
##            if i==j: continue
##            print(phone_book[i]+","+phone_book[j][:l2])
##            if phone_book[i] == phone_book[j][0:l2]:
##                return False
##        
##    
##    return answer


def solution(phone_book):
    answer=True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        print(phone_book[i]+","+phone_book[i+1][:len(phone_book[i])])
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
