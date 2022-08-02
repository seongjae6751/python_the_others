height1 = [int(h) for h in input("신장 연속 입력 : ").split()]
print("입력된 신장    :", height1)
height2 = height1.copy()

# 최대값을 활용한 선택정렬
for i in range(len(height1) - 1, 0, -1):
    max_index = 0
    for j in range(1, i + 1):
        if height1[j] > height1[max_index]:
            max_index = j
    print('debug : ', i, height1)
    height1[i], height1[max_index] = height1[max_index], height1[i]

# 유니폼 사이즈 리스트 0으로 채운 틀 만들기
small, medium, large = [], [], []
for i2 in range(len(height1)):
    if i2 % 3 == 0 :
        small.append(0)
    elif i2 % 3 == 1 :
        medium.append(0)
    elif i2 % 3 == 2:
        large.append(0)

# 0으로 채운 리스트 알맞는 값들로 수정
small[0:] = height1[:len(small)]
medium[0:] = height1[len(small):+len(small)+len(medium)]
large[0:] = height1[len(small)+len(medium):]

# 신장 사이즈를 유니폼 사이즈로 맞는 값들로 수정
for i3 in range(0, len(height2)):
    if height2[i3] in small:
        height2[i3] = str('S')
    elif height2[i3] in medium :
        height2[i3] = str('M')
    elif height2[i3] in large :
        height2[i3] = str('L')

print("유니폼 사이즈  :", height2)
print('small : ', small)
print('medium : ', medium)
print('large : ', large)
