def solution(numbers):

    answer=''
    
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)

    for n in numbers:
        answer+=n
    
    return str(int(answer))

print(solution([6,10,2]))
print(solution([3,30,34,5,9]))
print(solution([67,676,677]))
