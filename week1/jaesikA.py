n = int(input())
arr = []
cnt = 0
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    check = 0
    if arr[i] < 2:
        continue
    else:
        for j in range(2, arr[i] + 1):
            if arr[i] % j == 0:
                check = check + 1
    if check == 1:
        cnt = cnt + 1
print(cnt)