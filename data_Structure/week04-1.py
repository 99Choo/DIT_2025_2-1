# 함수 : 
# 호출에 의해 실행되는 일련의 코드 블록
# 호출 시 데이터를 전달 가능 : 파라메터(인수, 매개변수)
# 함수 처리 결과로 값을 반환 가능
# 파라메터는 여러 개 가능
# 파라메터 개수를 미리 알 수 없는 경우
# def myFruits(*fruits):
# 함수는 처리 결과로 반환 값을 가능

# 함수 정의 방법
# def 함수명(매개변수, ...):
# 함수 코드 블록

# 함수 정의와 호출 예

def printHello():
    print("Hello Python!!")

#---------------------------

def sayHello(name = "홍길동"):
    print(f"안녕하세요. {name}씨, 반갑습니다.")

#---------------------------

def intro(age, name = "홍길동"):
    print(f"저는 {age}세, {name}입니다.")

#---------------------------

def myFruits(*fruits):  # 호출 시 전달되는 인수들은 list에 담겨 fruits에 전달된다.
    for item in fruits:
        print(f"I like {item}.")

#---------------------------

def average(*val): # 매개변수 넘어온 값들의 평균을 출력하기
    """
    s = 0
    for item in val:
        s = s + item
    print(s/len(val))
    """
    print(sum(val)/len(val))


#---------------------------

def avg(a,b):
    return (a+b)/2

#---------------------------

def calc(a, b): # 사칙연산 결과값 4개를 반환하기
    return a+b, a-b, a*b, a/b

#---------------------------

#---------------------------

#---------------------------

#함수호출 
# printHello()
# sayHello("홍길동")
# intro("홍길동", 20)
# intro(age=30, name="이순신")
# myFruits("apple", "kiwi", "banana", "mango")
# average(1,2,3,5)
# sayHello("강감찬")
# intro(20)
# print(avg(3,4))
a = calc(3, -5)
print(a[0])
a,b,c,d = calc(3, 5)
a, *b, c = calc(3, 5)
def cac(a,b):
    return [a+b, a-b, a*b, a/b]
print(cac(3,4))