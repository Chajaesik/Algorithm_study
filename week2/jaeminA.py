n = int(input())
arr = [0] * n
sum = 0
top = -1

for i in range(n):
    m = int(input())
    if m == 0:
        arr[top] = 0
        top -= 1
    else:
        top += 1
        arr[top] = m

for i in range(top+1):
    sum += arr[i]

print(sum)