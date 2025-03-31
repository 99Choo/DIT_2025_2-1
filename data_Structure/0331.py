lst = [1,2,3,4,5]
type(lst)

lst = [10,20,30,40,50]
print(lst)

lst[2] = 300
print(lst)

lst.append(60)
# append = 맨뒤에 추가한다.
print(lst)

lst.insert(2, 25) 
# 300자리에 넣을려면 중간에 추가
print(lst)

lst.pop()
print(lst)
# 뒤에꺼면 꺼내기

lst.remove(50)
print(lst)
# 원하는 값 삭제

# lst.remove(50)
# print(lst)
# 없는 것을 삭제하러면 에러

lst.count(10)
print(lst)
# 해당값이 몇개 들어있는지

lst.append(20)
lst.append(20)
print(lst)
# 두번추가하면 
lst.count(20)
print(lst)
# 몇개 있는지 알려준다.
lst.index(300)
#안에 있는 인덱스 위치를 알려준다.

lst.insert(lst.index(40), 35)
print(lst)
#추가하고싶은 자리 위치를 모를때
lst2 = lst
print(lst2)
#값이 같이 바뀜(가르키는게 같다.)
lst2 = lst
#다름. 
lst2 = lst.copy()
lst2[1] = 200
print(lst)

lst.clear()
print(lst)

lst = ["apple", "kiwi", "mango"]
print(lst)

lst.extend(lst2)
print(lst)
#리스트에 다른 리스트  추가

lst.append(lst2)
print(lst)
#리스트 안에 리스트형태 추가

lst2.reverse()
print(lst2)
# 거꾸로 재배열 

lst2.sort()
print(lst2)

lst2.sort(reverse=True)
print(lst2)

lst = ["kiwi", "mango", "banana", "apple", "pineapple", "greengrape"]
print(lst)

len(lst[0])
print(lst)
len(lst[1])
print(lst)

lst.sort(key=len)
print(lst)
lst.sort(key=len, reverse=True)
print(lst)

lst = [10,20,30,40,50]
tpl = (10,20,30,40,50,20)
#항목 변경 불가 
print(tpl)

print(tpl[0])

a = list(tpl)
print(a)

a.pop()
print(a)

tpl = tuple(a)
print(tpl)

# 항목에 대한 변경 필요시 list로 변환
# Set 변수 하나에 여러 개의 값을 저장하는 4개 유형 중 하나
# st = {item, item2, ...}
# Set 항목 조건:
# 순서 없음 / 항목 변경 불가능 / 항목 중복 불가

b = {10,20,30,40,50}
print(b)
# print(b[0]) 에러 발생
b.add(60)
print(b)
# 추가
b.remove(60)
print(b)
# 삭제
b.discard(70)
print(b)

b.discard(50)
print(b)

b.pop()
# 순서가 없으니 아무꺼나 꺼낸다.
print(b)

c = {10,20,30,40,50}
d = {30,40,50,60,70}
c.intersection(d)
print(c)

cintd = c.intersection(d)
print(cintd)

cc = c.copy()
print(cc)

c.intersection_update(d)
print(c)

c ==  cc.copy
d == cc.copy

print(c)
print(d)

c.difference(b)
c.difference_update(d)
print(d)

c.union(cintd)
print(c)

#update 붙으면 원본 변경 아닐시 원본 유지 사본

c.update(cintd)
print(c)

cintd.issubset(c)
print(c)

d.issubset(c)
print(d)

c.issuperset(cintd)
print(c)

c.issuperset(d)
print(c)

# Dictionary
# 항목 중복 불가

q = {"Korea":"Seoul", "Japan":"Tokyo", "China":"Beijing", "France":"Paris"}
print(len(q))

q["China"] = "Seoul"
print(q)

q["Canada"] = "Toronto"
print(q)

q.pop("France")
print(q)

q.popitem()
print(q)

nation, capital = q.popitem()
print(nation)
print(capital)

t = q.popitem()
print(t)

q["Japan"]="Tokyo"
q["China"]="Beijing"

print(q.keys())

print(q.values())