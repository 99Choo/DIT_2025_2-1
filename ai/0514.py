"""
  함수 문서화 연습 
"""

def sumList(lst):
    """
    - 매개변수 lst(list)에 담긴 항목들의 합계를 계산하여 반환한다.
    - 사용법: sumList(lst)
    - 개발자: 홍길동 
    """    
    return sum(lst)


def greet(name):
    """
    넘겨받은 이름의 사람에 인사말을 다음과 같이 출력한다.
    name: 인사를 받을 사람의 이름
    출력: 안녕하세요 홍길동님. 
    return: None
    """
    print(f"안녕하세요 {name}님")

#===============================================================
def htmlCode(tag, text, className):
    """
    HTML 코드를 생성하여 출력한다.
    매개변수:
              tag: HTML Tag Name
             text: Tag에 포함될 내용 <tag>text...</tag>
        className: class 속성값.
    반환값: 없음.
    """
    print(f"<{tag} class='{className}'>{text}</{tag}>")
#===============================================================
def averageAll(*args):
    """
    매개 변수로 전달된 값들의 평균을 계산하여 반환한다.
    매개 변수: 임의의 개수의 수(number)
    반환값: 평균값
    """
    return sum(args) / len(args)
#===============================================================
# print(averageAll(2, 3))
# print(averageAll(2, 3, 15))
# print(averageAll(2, 3, 154, 435))
#===============================================================
def dispInfo(**kargs):
    """
    매개변수명과 매개변수의 값이 자유롭게 지정되어 전달가능한 형식의 함수
    함수 호출 시 전달한 매개변수명과 매개변수값은 dictionary로 저장되어 전달된다.
    """
    for key, value in kargs.items():
        print(f"{key}:[{value}]")
#===============================================================
# htmlCode("div", "인공지능프로그래밍기초", "title")
#===============================================================
def area(**kwargs):
    keys = set(kwargs.keys())

    if keys == {'radius'}:
        r = kwargs['radius']
        print(3.14 * r * r)

    elif keys == {'width', 'height'}:
        print(kwargs['width'] * kwargs['height'])

    elif keys == {'width'} or keys == {'height'}:
        val = kwargs.get('width') or kwargs.get('height')
        print(val * val)

    else:
        print("Error: 잘못된 인자 조합입니다.")
#===============================================================
area(width=10, height=20)
#===============================================================
# area(width=100, height=200)
# area(radius=10)            # 3.14 *10*10
# area(width=10)             #10 x 10 (정사각형)
# area(height=10)            #10 x 10 (정사각형)
# area(radius=10, height=10) # 오류
# area(radius=10, width=10)  # 오류 
#===============================================================

def sumAvg(a,b):
    return a+b, (a+b)/2



      

                        