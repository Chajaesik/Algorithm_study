stack = []  #stack의 이름을 가진 array 생성
top = -1    #stack의 초기값 -1로 하지않으면 값을 push, pop 할 때 index값이 달라지게 됌
sum = 0     #array 값들의 합
n = int(input())        #입력 할 수의 개수

for i in range(n):
    num = int(input())
    if num > 0:
        top +=1         #여기서 top의 값을 추기하기 때문
        stack[top].append(num)
    elif num == 0:
        stack[top].pop(num)
        top -= 1        #여기서 top의 값을 빼야하기 때문, top의 순서가 바뀐다면 전 인덱스의 값이 사라질 수 있음
    elif num < 1 and num > 100000:
        print("값 다시 입력")

for i in range(len(stack)):     #stack 배열의 길이만큼 반복하여 배열의 합을 얻음
    sum += stack[i]
print(sum)