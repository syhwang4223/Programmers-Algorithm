import copy

def solution(expression):
    answers = []
    operand = []
    operator_orig = [] # *, +, -

    for o in expression:
        if o == "*" or o=="+" or o=="-":
            operator_orig.append(o)

    operand = expression.replace("+","*").replace("-","*").split("*")
    operand_orig = list(map(int,operand))


    # *+-  순서
    def multiple():
        for o in operator_orig:
            if o=="*":
                i = operator.index(o) 
                operand[i]=operand[i]*operand[i+1]
                if len(operator)==1: answers.append(abs(operand[i]))
                operator.pop(i)
                operand.pop(i+1)

    def plus():
        for o in operator_orig:
            if o=="+":
                i = operator.index(o) 
                operand[i]=operand[i]+operand[i+1]
                if len(operator)==1: answers.append(abs(operand[i]))
                operator.pop(i)
                operand.pop(i+1)

    def minus():
        for o in operator_orig:
            if o=="-":
                i = operator.index(o)
                operand[i]=operand[i]-operand[i+1]
                if len(operator)==1: answers.append(abs(operand[i]))
                operator.pop(i)
                operand.pop(i+1)

    operand=operand_orig.copy()
    operator=operator_orig.copy()
    multiple()
    plus()
    minus()

    operand=operand_orig.copy()
    operator=operator_orig.copy()
    multiple()
    minus()
    plus()
    
    operand=operand_orig.copy()
    operator=operator_orig.copy()
    plus()
    multiple()
    minus()

    operand=operand_orig.copy()
    operator=operator_orig.copy()
    plus()
    minus()
    multiple()  

    operand=operand_orig.copy()
    operator=operator_orig.copy()
    minus()
    multiple()
    plus()

    operand=operand_orig.copy()
    operator=operator_orig.copy()
    minus()
    plus()
    multiple()

    print(answers)

    return max(answers)
