def solution(s):
    tmp = []

    for alpha in s:
        if not tmp or tmp[-1] != alpha:
            tmp.append(alpha)
        elif tmp[-1] == alpha:
            tmp.pop()
    if not tmp: return 1
    else: return 0
            


print(solution("baabaa"))             
print(solution("cdcd"))
print(solution("acccca"))


