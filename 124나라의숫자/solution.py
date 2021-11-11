def solution(n):
    answer = ''
    number = ['1','2','4']

    
    while n>0:
        n -= 1 
        answer = number[n%3] + answer
        n = n//3
    return answer

print(1,1,solution(1))
print(2,2,solution(2))
print(3,4,solution(3))
print(4,11,solution(4))
print(5,12,solution(5))
print(6,14,solution(6))
print(7,21,solution(7))
print(8,22,solution(8))
print(9,24,solution(9))
print(10,41,solution(10))


