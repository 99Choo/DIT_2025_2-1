"""
양수,정수,홀수 판별기
"""
a = int(input("정수 입력:"))

if a > 0:
    if a % 2 > 0:
        print(f"{a}는 홀수")
    else:
        print(f"{a}는 짝수")
            
else:
    print("양수가 아님")
"""
소수 찾기
"""
b = int(input("정수 입력"))

if b < 1 or b > 10:
 print("잘못된 입력")
elif b==2 or b==3 or b==5 or b==7:
 print("소수")
else:
 print("소수아님")
