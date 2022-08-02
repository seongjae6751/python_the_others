height1 = [171, 172,167, 192, 165, 169, 170, 178, 177, 159]
height2 = [171, 172,167, 192, 165, 169, 170, 178, 177, 159]

for i in range(len(height1) - 1, 0, -1):
    max_index = 0
    for j in range(1, i + 1):
        if height1[j] > height1[max_index]:
            max_index = j
    height1[i], height1[max_index] = height1[max_index], height1[i]

small = []
medium = []
large = []

for i2 in range(len(height1)):
    if i2 % 3 == 0 :
        small.append(0)
    elif i2 % 3 == 1 :
        medium.append(0)
    elif i2 % 3 == 2:
        large.append(0)

small[0:] = height1[:len(small)]
medium[0:] = height1[len(small):+len(small)+len(medium)]
large[0:] = height1[len(small)+len(medium):]

SizeDict = dict() # 입력된 신장 -> 딕셔너리 제작 (사진 참고)
for i in small : # SizeDict['small에 있는 원소 하나'] = 'S'  / 원소가 160 이면 {'160' : 'S'} 만들어짐
    SizeDict[i] = 'S'
    print(SizeDict) # 출력하면서 변화 관찰하기
for i in medium :
    SizeDict[i] = 'M'
for i in large :
    SizeDict[i] = 'L'
    
print('만들어진 사전 : ' ,SizeDict)
cnt=0
for i in height2 : # 딕셔너리 -> 입력된 신장  (사진 보내준거 참고)
    height1[cnt] = SizeDict[i] # ex. SizeDict[159]는 S가 리턴된다. height2의 0번째 위치에 S가 넣어짐.
    cnt +=1 # 알겠지..? 왜 하는지...?


print("입력된 신장 : ", height2)
print("유니폼 사이즈 : ", height1 )
print('small : ', small)
print('medium : ', medium)
print('large : ', large)