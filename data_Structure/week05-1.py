Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Person:
...     name = "홍길동" # 속성 정의
...     #메소드 정의
...     def intro(self):
...         print(f"저는 {self.name}입니다.")
... 
...         
>>> #==============================================
...         
>>> # 객체 생성하기
>>> p = Person()
>>> p.intro()
저는 홍길동입니다.
