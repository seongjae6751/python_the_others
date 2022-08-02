import random
first_class = []
second_class = []
third_class = []
while True:
        if len(first_class) and len(second_class) and len(third_class) == 40:
            break
        def append_list(a):
            b = random.randint(1,100)
            a.append(b)
        
        append_list(first_class)
        append_list(second_class)
        append_list(third_class)

def class_grade(c):
    print("리스트는", c)
    print("평균은", sum(c) / len(c))
    c.sort()
    print(c)
    print("최고점은", c[39])
    print("최저점은", c[0])

class_grade(first_class)
class_grade(second_class)
class_grade(third_class)