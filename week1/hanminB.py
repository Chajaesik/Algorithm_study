num1 = int(input())     #2가지 수 입력
num2 = int(input())
cntMin = 0              #소수의 개수
arr = []                #소수를 저장하기 위한 배열

for i in range(num1, num2):     #입력한 두 수 사이의 for문
        for j in range(1, i + 1):       #num1인 i값을 나눠줌 
            if i % j == 0:              
                cntMin += 1
        if cntMin == 2:
            arr.append(j)               #arr에 값 추가
        cntMin = 0

for i in range(len(arr)):       #arr의 개수만큼 반복하여 출력
     print(arr[i]) 