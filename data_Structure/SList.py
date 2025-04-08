#=================================
# 단순 연결 리스트 (Singly Linked List)
#=================================
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
#=================================
class SList:
  def __init__(self):
    self.head = None                      # SList의 첫 노드를 가리킨다. (초기값은 빈 리스트이므로 None)
    self.count = 0                        # SList에 연결된 노드의 개수 (를 항상 유지한다.)
    #-----------------------------
                                          # 기존의 리스트 맨 뒤에 새 노드(newNode)를 연결한다.
  def append(self, newNode):
      if self.head is None:               # SList가 빈 리스트인 경우
          self.head = newNode             # 추가하려는 새 노드(newNode)가 첫 노드가 된다. 
          self.count = 1
      else:                               # 1개 이상의 노드가 있는 경우, (마지막 노드를 찾아서 그 뒤에 newNode를 연결한다.)
          current = self.head             # 리스트의 첫 노드(self.head)부터 순서대로 확인하면서 마지막 노드를 찾는다.
          while current.next is not None: # 현재 노드(current)의 다음 노드가 있으면 
             current = current.next       #current는 다음 노드를 가르키도록 설정한다. 
                                          # current.next가 None이면 while 종료, ==> current가 마지막 노드임을 의미 
                                          # 새 노드(newNode)를 current 뒤에 연결한다.
          current.next = newNode
                                          # 새 노드가 추가되었으므로 self.count 값 변경
          self.count += 1          
#==================================
  # 리스트의 현재 연결 상황을 출력한다.
  # 빈 리스트의 경우: [Empty]
  # 그 외의 경우 [100]-[200]-...-[300]-[None] 형식으로 출력 예정 
  def showList(self):
     print("Head->", end="")            # 초기 정보를 출력하고 줄바꿈 하지 않음. (-> 다음 이어질 출력과 연결)
     current = self.head                  # 리스트의 첫 노드부터 차례대로 방문하며 노드 값을 출력하기
     while current is not None:
        print(f"[{current.data}]-", end="") # 현재 노드(current)의 data를 출력.
        current = current.next            # 현재 노드의 위치를 다음 노드로 이동 

        print(f"||({self.count} nodes.)")
  #--------------------------------
  def appendValue(self, value):
      self.append(Node(value))
     
#==================================
lst = SList() # 빈 리스트 하나 생성.
lst.showList()
lst.appendValue(200)
lst.appendValue(40)
lst.appendValue(60)
lst.appendValue(2400)
lst.appendValue(1200)
lst.showList()
#lst.append(n2)
lst.showList()

#==================================
