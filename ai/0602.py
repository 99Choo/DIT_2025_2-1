class Test:
  def __init__(self, value1, value2):
    self.a = value1
    self.b = value2
  
  def __str__(self):
    return f"({self.a}, {self.b})"

class People:
  def __init__(self, name):
    self.name = name
  def sayHello(self):
    print(f"Hello, My name is {self.name}")

p1 = People("Hong")
p2 = People("Kim")
p1.sayHello()
p2.sayHello()
People.sayHello(p1)
People.sayHello(p2)

# 클래스 정의 밖에서 객체 생성
t = Test(10, 20)
t2 = Test(100, 200)

del t2.a       # t2 객체의 a 속성 삭제
t.c = 100      # t 객체에 새로운 속성 c 추가

print(f"t.a = {t.a}, t.b={t.b}, t.c={t.c}")


