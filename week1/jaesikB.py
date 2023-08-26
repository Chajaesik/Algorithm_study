n = int(input())
m = int(input())

arr = [True] * (m + 1)  # True의 값을 m + 1의 사이즈까지 초기화

for i in range(2, int(m**0.5) + 1): # 나열된 수를 제거하는 최대 배수는 무조건 m의 제곱근 이하 100 -> 10
    if arr[i]:
        for j in range(2 * i, m + 1, i): # 2의 배수부터 제거
            arr[j] = False

for i in range(n, m + 1):
    if arr[i]:
        print(i)