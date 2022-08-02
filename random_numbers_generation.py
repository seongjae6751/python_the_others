import random
a = int(input("30이상의 수를 입력하시오:"))
if a < 30:
    print(' 30이상의 수를 입력하시오')
else:
    item_count = []
    while True:
        if item_count.count(a) == 1000:
            break
        b = random.randint(0, a)
        item_count.append(b)
    for c in range(0, a+1):
        print('{}의 개수는 {}입니다'.format(c, item_count.count(c)))
print('0 부터 입력한 숫자가 1000번 발생할때가지 총 반복회수는 {}입니다.'.format(len(item_count)))

import random
inputNum = int(input("30 이상의 숫자를 입력하세요 : "))  # input()
flag = False
count = 0
numbers_set = [0 for i in range(0, inputNum + 1)] # 1~30의 리스트 생성
# number_set의 첫번째 원소는 숫자 1이 발생한 횟수를 의미한다.
# 즉 두번째 원소는 수자 2가 발행한 횟수를 의미하고
# 영번째 원소는 숫자 0이 발행한 횟수를 의미한다.
while(flag == False): # flag가 true일때 종료
    count += 1
    rand = random.randint(0, inputNum) # 랜덤 숫자 생성
    numbers_set[rand] += 1 # 랜덤 숫자의 위치에 +1
    if numbers_set[inputNum] >= 1000:  # input한 숫자의 리스트 위치가 10000 이상일 때 조건문 실행
        for i in range(0,inputNum+1) :
            print(i, "이 발생한 횟수는 ", numbers_set[i], "입니다.")
        flag = True
        print("0부터 입력한 숫자 ", inputNum, " 이 1000번 발생할때까지의 총 반복회수는", count, "번 입니다.")

