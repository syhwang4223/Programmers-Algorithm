import math
import itertools


def isPrime(n):
    if n==0 or n==1 :return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:return False

    return True

def solution(numbers):
    answer = []
 
    nums = list(numbers) #주어진 문자열을 char 배열로 분할
    permutations = [] #순열을 담을 배열
    
    #주어진 종이로 가능한 모든 순열
    for i in range(1,len(nums)+1):
        permutations += list(itertools.permutations(nums,i))

    #순열이 소수이면 정답 리스트에 추가
    for p in permutations:
        p = ''.join(p)
        if isPrime(int(p)):
            answer.append(int(p))
    
    #answer 리스트의 중복값 제거
    answerSet = set(answer)
    print(answerSet)
       
    return len(answerSet)

