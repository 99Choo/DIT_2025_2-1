# a = {1, 2, 3}
# b = {2, 3, 4}

# a.update(b)
# print(a)
# print("=================")

# t = (10, 20)
# a.update(t)

# print(a)
# print("=================")

# d = {"a":100, "b":200}
# a.update(d)
# print(a)
# print("=================")

# l = [1,2,3]
# l.append(a)
# l.append((10,20))
# print(l)
# print("=================")


# s = {1,2}
# s.add((10,20))
# print(s)
# print("=================")

# # 모양 자체로 들어가는 add, 분리해서 들어가는 update

# class Point:
#     x = 10
#     y = 20

# p = Point()
# s.add(p)
# print(s)
# print("=================")

# hash(p)

# a = {1,2,3}
# b = {2,3,4}
# print(a.union(b))
# print("=================")
# u = print(a.union(b))

# c = [2,3,4]
# print(a.union(c))
# print("=================")
# print (a.union([2,2,3,4,2,1]))

# print(a | b)
# print(a & b)
# print(a - b)
# # print(a + b) 안됨.
# print("=================")


# a = {1,2,3}
# b = {2,3,4}
# c = {4,5,6}
# print(a & b)
# print(a | b)
# print(a - b)
# print(b - a)
# print(a ^ b)

# a ^=b
# print(a)


def triple_symmetric_difference(a,b,c):
 e = (a^b^c) - (a&b&c)
 print(e)

a = {1,2,3,4}
b = {2,4,5,6}
c = {3,4,6,7}
triple_symmetric_difference(a,b,c)
# print("=================")
def common_item(ls1, lst2):
 return list(set(ls1) & set(lst2))
print(common_item([1,2,3],[2,3,4]))

d = {"a":1, "b":2}
d2 = dict(a=1, b=2, c=2)
print(d2)

#d3 = dict("a"=a, "b"=2)
a= "Korea"
d3=dict(a=1,b=2)
print(d3)