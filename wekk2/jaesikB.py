
n = int(input())
postfix = input()
stack = []
num = []
result = 0
for i in range(n):
    num.append(int(input()))

for i in postfix:
    if i >= 'A' and i <= 'Z':
        stack.append(num[ord(i)-65])
    else:
        s1 = stack.pop()
        s2 = stack.pop()

        if i == '*':
            s2*=s1
        elif i == '/':
            s2/=s1
        elif i == '+':
            s2+=s1
        elif i == '-':
            s2-=s1
        stack.append(s2)
print(format(stack[0],".2f"))