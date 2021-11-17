
def isCorrect(p):#주어진 문자열이 올바른 괄호 문자열인지 판단하는 함수
    st = []
    for bracket in p:
        if not st and bracket==')':
            return False
        elif not st:
            st.append(bracket)
        elif st[-1]=="(" and bracket==")":
            st.pop()
        else:
            st.append(bracket)

    if st : return False
    else : return True

def seperate(p):#주어진 문자열을 조건에 맞게 u,v로 나눠주는 함수
     
    if p=="": return "",""
    left,right=0,0

    for i in range(len(p)):
        if p[i]=='(': left+=1
        else: right+=1

        if left==right:
            u=p[:i+1]
            v=p[i+1:]
            
            return u,v
                
                

            

def solution(p):
    answer=''
    
    if isCorrect(p): return p

    u,v=seperate(p)
    
    while u:
        if not isCorrect(u):
            answer+="("+solution(v)+")"

            u=u[1:-1]
  
            u=u.replace("(","t")
            u=u.replace(")","(")
            u=u.replace("t",")")
 
            return answer+u
        else:
            answer+=u
            u,v=seperate(v)

                
   
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution("))()(("))



