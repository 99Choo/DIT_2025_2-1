class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return f"[{self.data}]"

class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        newNode = Node(value)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.count += 1

    def insertFront(self, value):
        newNode = Node(value)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.count += 1

    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def insertBefore(self, targetNode, value):
        if targetNode is None:
            return
        newNode = Node(value)
        if targetNode == self.head:
            self.insertFront(value)
        else:
            prevNode = targetNode.prev
            prevNode.next = newNode
            newNode.prev = prevNode
            newNode.next = targetNode
            targetNode.prev = newNode
            self.count += 1

    def insertAfter(self, targetNode, value):
        if targetNode is None:
            return
        newNode = Node(value)
        if targetNode == self.tail:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            nextNode = targetNode.next
            newNode.next = nextNode
            newNode.prev = targetNode
            targetNode.next = newNode
            nextNode.prev = newNode
        self.count += 1

    def insertSorted(self, value):
        current = self.head
        while current:
            if value < current.data:
                self.insertBefore(current, value)
                return
            else:
                current = current.next
        self.append(value)

    def remove(self, targetNode):
        if targetNode is None:
            return
        if self.count == 1:
            self.head = None
            self.tail = None
        elif targetNode == self.head:
            self.head = targetNode.next
            self.head.prev = None
        elif targetNode == self.tail:
            self.tail = targetNode.prev
            self.tail.next = None
        else:
            prevNode = targetNode.prev
            nextNode = targetNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
        self.count -= 1

    def showList(self):
        print("head->", end="")
        current = self.head
        while current:
            print(current, end="-")
            current = current.next
        print(f"({self.count} nodes)")

    def isEmpty(self):
        return self.count == 0
