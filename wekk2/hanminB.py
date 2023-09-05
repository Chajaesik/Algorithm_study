n = int(input())        #피연산자의 개수
post = input()          #후위표기식
num = []                #숫자값 또는 영어값

for i in range(n):
    num.append(int(input()))
stack = []
for i in post:      #post라는 문자열의 값들을 값들만큼 반복
    if i >= 'A' and i <= 'Z':        #post에서 ABC*+DE/-라면 차례대로 A는 num[0]의 인덱스
        stack.append(num[ord(i)-65]) #B는 num[1]의 인덱스로 처리됨 즉, stack 배열에 숫자값 추가
    else:
        s2 = stack.pop()  #s1, s2순서로 pop하게 되면 stack의 특성에 의해 값이 변할 수 있음  
        s1 = stack.pop()

        if i == '*':                #후위표기식을 따라가기 때문에 우선순위는 상관 x  
            stack.append(s1 * s2)   
        elif i == '/':
            stack.append(s1 / s2)
        elif i == '+':
            stack.append(s1 + s2)
        elif i == '-':
            stack.append(s1 - s2)
print(format(stack[0],".2f"))

