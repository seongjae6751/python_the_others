a = int(input("행의 개수 입력>>"))
b = int(input("열의 개수 입력>>"))
c = 300
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if j % 2 == 1:
            print(c, end ='')
            c += 1
        else:
            print(' -X- ', end ='')
    print()
print("시험장 가용인원:", c - 300, '명')