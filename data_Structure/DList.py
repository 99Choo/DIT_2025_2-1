"""
    이중 연결 리스트 (Double Linked List)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"[{self.data}]"


class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        newNode = Node(data)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.count += 1

    def showList(self):
        print("head", end="->")
        current = self.head
        while current:
            print(current, end="-")
            current = current.next
        print(f"({self.count} nodes)")

    def insertFront(self, data):
        if self.count == 0:
            self.append(data)
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.count += 1

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                break
            else:
                current = current.next
        return current

    def insertBefore(self, targetNode, data):
        if targetNode is None:
            return
        if self.head is targetNode:
            self.insertFront(data)
        else:
            newNode = Node(data)

            newNode.next = targetNode
            newNode.prev = targetNode.prev
            targetNode.prev.next = newNode
            targetNode.prev = newNode

            self.count += 1

    def insertAfter(self, targetNode, data):
        if targetNode is None:
            return
        newNode = Node(data)

        if targetNode.next is not None:
            newNode.prev = targetNode
            newNode.next = targetNode.next
            targetNode.next.prev = newNode
            targetNode.next = newNode
        else:
            targetNode.next = newNode
            newNode.prev = targetNode
            self.tail = newNode  # tail 갱신

        self.count += 1

    def remove(self, targetNode):
        if targetNode is None:
            return

        if self.count == 1:
            self.head = None
            self.tail = None
        elif targetNode == self.head:
            self.head = targetNode.next
            if self.head:
                self.head.prev = None
        elif targetNode == self.tail:
            self.tail = targetNode.prev
            if self.tail:
                self.tail.next = None
        else:
            targetNode.prev.next = targetNode.next
            targetNode.next.prev = targetNode.prev

        self.count -= 1
        del targetNode

    def isEmpty(self):
        if self.count == 0:
            return True
        return False
    

# # 테스트 코드 예시
lst = DList()
lst.append(10)
# lst.append(20)
# lst.insertFront(5)
# lst.insertBefore(lst.find(20), 15)
# lst.insertAfter(lst.find(10), 12)
# lst.show()
# lst.remove(lst.find(15))
lst.showList()
