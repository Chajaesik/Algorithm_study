num = 0
number = 0
cntMin = 0  #몫의 개수
cnt = 0     #몫이 두개인 경우(소수) 추가

while not(num >= 1 and num <= 100):   #개수가 100개 이하인 조건
    num = int(input())

for i in range(1, num+1):       #1부터 n+1까지
    while not(number >= 1 and number <= 1000):   #개수가 100개 이하인 조건
        print("1,000 이하의 자연수를 입력")
        number = int(input())
    for i in range(1,number + 1):
        if number % i == 0:     #입력받은 수와 i 값을 나눴을 때 나머지가 0인 경우 cntMin의 개수 추가 
            cntMin += 1
    if cntMin == 2:     #cntMin이 2개인 경우 소수로 판단하여 cnt에 추가
        cnt +=1 
    cntMin = 0
    number = 0
        
print("소수의 개수", cnt) 