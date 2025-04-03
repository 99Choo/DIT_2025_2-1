lst = [1,2,2,3,4,3,2,5]
print([(item, lst.count(item)) for item in set(lst)])

# 항목과 항목의 등장 회수를 튜플(항목, 회수)로 표현
# 저장한 리스트를 생성

a, b, c = (1,2,3)
print(a+b+c)

t = (1, [2, 3], 4)
t[1].append(5)
print(t)

t1 = (1,2)
t2 = (1,2,4)
print(t1<t2)

