#====================================================
# 이중 연결 리스트를 이용하여 스택(stack) 구현하기
#====================================================
from DList import *
#====================================================
class StackUnderFlow(Exception):
  pass

class Stack(DList):

  # 스택에 새 데이터를 추가하는 연산
  def push(self, value):
    self.insertFront(value) #DList의 append 메서드 사용
    

  # 스택에 맨 위에 있는 데이터를 가져오는 연산 (맨 위의 데이터는 스택에서 제거됨)
  def pop(self):
    if self.isEmpty():
     raise StackUnderFlow("Stack Empty!!")
    else:
      returnValue = self.head.data
      self.remove(self.head)
      return returnValue

  # 스택이 비었는지 확인하는 연산 (반환값: True: 빈 스택, False: 데이터가 있음.)
  def isEmpty(self):
   if self.count == 0:
     return True
   return False

  # 스택 맨 top 항목의 값을 일어오는 연산 (읽은 항목이 제거 되지 않음. pop() 비교)
  def peek(self): 
    if self.isEmpty():
     raise StackUnderFlow("Stack Empty")
    return self.head.data

#====================================================
# 괄호 매칭이 순서대로 되었는지를 확인하는 함수
# 사용 가능한 괄호: (), {}, [], <> 예: "{()<<>>[[]]}"
# 반환값: True : 매칭이 잘 되었을 경우, False: 매칭에 문제가 발생했을 경우,
def checkParenthese(st):
    print("{st}: ", end="")

    pleft = "(>{["
    pright = "]})"
    pairs = "()<>{}[]"

    stack = Stack()

    for item in st:         # 현재 문자가 왼쪽 괄호이면 
      if item in pleft:     #
       stack.push(item)     # 
      elif item in pright:  # 현재 문자가 오른쪽 괄호이면
        top = stack.pop()   # 스택에서 위에 있는 값을 꺼내온다.
        if (top + item) in pairs:
          continue          # 다음 문자 처리하러 반복문 계속.
        else:
          print(f"매칭 오류 발생: {top}, {item}")
          return False
      else:
        continue

      if not stack.isEmpty():   # 닫히지 않은 왼쪽 괄호가 스택에 남아 있는 상황이므로
        print("닫히지 않은 괄호가 남아 있습니다.")
      return False
    return True

test_cases = [
    "{((<<>>[[]])})",   # ✅ 올바름 → True
    "{[()]}",           # ✅ 올바름 → True
    "{[(])}",           # ❌ 잘못된 순서 → False
    "<[{()}]>",         # ✅ 올바름 → True
    "(()",              # ❌ 닫는 괄호 없음 → False
    "",                 # ✅ 빈 문자열 → True
    "{[(()<>)]}",       # ✅ 복합 괄호 → True
    "{<([)]>}",         # ❌ 닫는 순서 잘못됨 → False
    "no brackets!",     # ✅ 괄호 없음 → True
]

print(checkParenthese(test_cases))



#stack = Stack()
#stack.push(100)
#stack.push(200)
#stack.showList()
#print(stack.pop())
#stack.showList()
#a = stack.peek()
#stack.showList()
