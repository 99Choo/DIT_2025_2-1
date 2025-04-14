#=================================
# 단순 연결 리스트 (Singly Linked List)
#=================================
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return f"[{self.data}]"

#=================================
class SList:
  def __init__(self):
    self.head = None                      # SList의 첫 노드를 가리킨다.
    self.count = 0                        # SList에 연결된 노드의 개수

  def __len__(self):
    return self.count

  # 기존의 리스트 맨 앞에 새 노드(newNode)를 추가한다.
  def insertFront(self, newNode):
    if self.head is None:
        self.head = newNode
        self.count = 1
    else:
       newNode.next = self.head
       self.head = newNode
       self.count += 1

  # 기존의 리스트 맨 뒤에 새 노드(newNode)를 연결한다.
  def append(self, newNode):
      if self.head is None:
          self.head = newNode
          self.count = 1
      else:
          current = self.head
          while current.next is not None:
             current = current.next
          current.next = newNode
          self.count += 1

  def appendValue(self, value):
      self.append(Node(value))

  # 리스트의 현재 연결 상황을 출력한다.
  def showList(self):
     print("Head->", end="")
     current = self.head
     while current is not None:
        print(f"{current}-", end="")
        current = current.next
     print(f"||({self.count} nodes.)")

  # 리스트의 첫 노드를 삭제하며 반환한다.
  def unshift(self):
     if self.head is None:
        return None
     else:
        header = self.head
        self.head = self.head.next
        header.next = None
        self.count -= 1
        return header

  # 리스트의 노드 연결 순서를 역순으로 재구성한다.
  def reverse(self):
     revList = SList()
     while self.head is not None:
        h = self.unshift()
        revList.insertFront(h)
     self.head = revList.head
     self.count = revList.count

  def reverse2(self):
     revHead = None
     while self.head is not None:
        next = self.head.next
        self.head.next = revHead
        revHead = self.head
        self.head = next
     self.head = revHead

  # 리스트의 정렬 상태를 유지하면서 새 노드를 추가한다.
  def insertSorted(self, newNode):
    if self.head is None or newNode.data < self.head.data:
        newNode.next = self.head
        self.head = newNode
    else:
       current = self.head
       while current.next is not None and current.next.data < newNode.data:
          current = current.next
       newNode.next = current.next
       current.next = newNode
    self.count += 1

  # 특정값을 가진 노드를 연결 리스트에서 제거한다.
  def remove(self, value):
     targetNode = self.find(value)
     if targetNode is None:
        return None
     else:
        previous = None
        current = self.head
        while current is not targetNode:
           previous = current
           current = current.next
        if previous is None:
          self.head = current.next
        else:
           previous.next = current.next
        current.next = None
        self.count -= 1
        return current

  # 특정값이 리스트에 포함되어 있는지 확인한다.
  def find(self, value):
    current = self.head
    while current is not None:
      if value == current.data:
        return current
      else:
        current = current.next
    return None

#==================================
# 테스트 실행 코드
lst = SList()
lst.insertFront(Node(100))
lst.insertFront(Node(200))
lst.insertFront(Node(300))
lst.showList()
lst.head.next.data = 1000
lst.showList()
lst.unshift()
lst.showList()
lst.reverse()
lst.showList()
lst.insertSorted(Node(250))
lst.showList()