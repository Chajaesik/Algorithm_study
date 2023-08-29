
n = int(input())
stack = [0] * 100001
top = -1
result = 0
for i in range(n):
    num = int(input())
    if num == 0:
        if top >= 0:
            stack[top] = 0
            top-=1
    else:
        top+=1
        stack[top] = num

for i in range(top+1):
    result+= stack[i]
print(result)

    