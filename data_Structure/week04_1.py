# 함수 정의 연습

def printHello():
    print("Hello Python!!")
#---------------------------------------------------
def sayHello(name="홍길동"):
    print(f"안녕하세요 {name}씨, 반갑습니다.")
#---------------------------------------------------
def intro(age, name="홍길동"):
    print(f"저는 {age}세, {name}입니다.")
#---------------------------------------------------
def myFruits(*fruits):  # 호출 시 전달되는 인수들은 list에 담겨 fruits에 전달된다.
    for item in fruits:
        print(f"I like {item}.")
#---------------------------------------------------
def average(*val):    # 매개변수 넘어온 값들의 평균을 출력하기.
    """
        s = 0
        for item in val:
            s = s + item
        print(s/len(val))
    """
    print(sum(val)/len(val))
#---------------------------------------------------
def avg(a, b):
    return (a+b)/2
#---------------------------------------------------
def calc(a, b): # 사칙연산 결과값 4개를 반환하기
    return a+b, a-b, a*b, a/b
#---------------------------------------------------
#함수 호출
print(avg(3,4))
