m = int(input())
n = int(input())
arr = [True] * (n + 1) #모든 배열에 일단 true 삽입

for i in range(2, int(n ** 0.5)): #최대값의 제곱근 까지만 반복
    if arr[i]:
        for j in range(2 * i, n + 1, i): #자신을 제외한 자신의 배수들 모두 false 삽입
            arr[j] = False
        
for i in range(m, n+1):
    if arr[i]:
        print(i) #출력

