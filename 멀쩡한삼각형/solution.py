from math import gcd

def solution(w,h):
    answer = w*h
    split = 0

    #구분구적법 -c에서는 되는데 파이썬에선 시간초과
    #for i in range(1,w+1):
    #   answer+= int(-(h/w)*i + h)

    #gcd
    g = gcd(h,w)
    if g==1:
        split = h + w - 1
    else:
        split = (h/g + w/g -1)*g
    
    
    return answer - split
