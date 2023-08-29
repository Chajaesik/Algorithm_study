cnt = 0

while True: #수의 개수 제한
    n = int(input())
    if n <= 100:
        break
    else:
        print("다시 입력하세요")

for i in range(n): 
    check = False

    while True: #m의 범위 제한
        m = int(input())
        if m <= 1000:
            break
        else:
            print("다시 입력하세요")

    for j in range(2, m): #소수 판별
        if m % j == 0:
            check = False
            break
        check = True

    if check: #소수 개수 세기
        cnt += 1
print(cnt)
    
