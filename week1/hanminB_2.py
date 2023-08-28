import math
n1 = int(input())   #시작값
n2 = int(input())   #끝 값
while n2<n1:        #n1 과 n2 의 입력값에 따른 예외처리
    n1 = int(input())   #시작값
    n2 = int(input())   #끝 값

arr = [True] * (n2 + 1)     #끝값 만큼의 배열을 생성하여 True값을 넣어줌

for i in range(2, int(math.sqrt(n2) + 1)): #값의 제곱근에 +1 한 값을 구하여 반복하면 더 간단함 > 어차피 배수면 소수가 아님 
    if arr[i]:          #0,1은 소수가 아니기 때문에 2부터 반복하여 제곱근 값까지 true를 검사함 
        for j in range(i * 2, n2 + 1, i):       #true면 소수란 뜻이고, i값 만큼 추가되는 for문으로 모든 배수의 값을 false로 변환
            arr[j] = False

for i in range(n1, n2 + 1):     #범위 내의 True인 값들을 차례대로 출력
    if arr[i]:
        print(i)        #인덱스 값을 출력하기 위해 arr[i]가 아닌 i 출력