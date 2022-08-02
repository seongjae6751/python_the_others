import random
grade_sample = [[0],[1],[2]]
def append_list(a):
        b = random.randint(1,100)
        a.append(b)
while True:
    if len(grade_sample[0]) and len(grade_sample[1]) and len(grade_sample[2]) == 40:
        break
    append_list(grade_sample[0])
    append_list(grade_sample[1])
    append_list(grade_sample[2])

for i in range(1,4):
    print("****************")
    print(i, "반 평균은", sum(grade_sample[i - 1]) / len(grade_sample[i - 1]))
    grade_sample[i - 1].sort()
    print("최고점은", grade_sample[i - 1][39])
    print("최저점은", grade_sample[i - 1][0])
    print("****************")

print(grade_sample)

