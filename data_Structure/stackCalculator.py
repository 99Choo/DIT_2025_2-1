from DList import *

class QueueUnderFlow(Exception):
    pass

class Queue(DList):
    def add(self, value):
        self.append(value)

    def remove(self):
        if self.isEmpty():
            raise QueueUnderFlow("Queue is Empty")
        returnValue = self.head.data
        super().remove(self.head)
        return returnValue

    @staticmethod
    def toTokens(strInfix):
        chList = list(strInfix)
        ops = "+-*/()"
        nums = "0123456789."
        numToken = ""
        tokenList = []

        while chList:
            ch = chList.pop(0)
            if ch in ops:
                tokenList.append(ch)
            elif ch in nums:
                numToken += ch
                while chList and chList[0] in nums:
                    numToken += chList.pop(0)
                tokenList.append(float(numToken))
                numToken = ""
            else:
                continue
        return tokenList

class Stack(DList):
    def push(self, value):
        self.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        value = self.tail.data
        self.remove(self.tail)
        return value

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.tail.data

priority = {'+': 1, '-': 1, '*': 2, '/': 2}

def infix2Postfix(lstInfix):
    stack = Stack()
    queue = Queue()

    while lstInfix:
        token = lstInfix.pop(0)
        if type(token) == float:
            queue.add(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while not stack.isEmpty() and stack.peek() != "(":
                queue.add(stack.pop())
            if not stack.isEmpty():
                stack.pop()
            else:
                raise Exception("Mismatched parentheses")
        else:
            while not stack.isEmpty() and stack.peek() != "(" and priority.get(stack.peek(), 0) >= priority[token]:
                queue.add(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        queue.add(stack.pop())

    return queue


def stackCalculator(queue):
    stack = Stack() # 계산용 stack 생성

    while not queue.isEmpty():
        token = queue.remove()
        
        if type(token) == float:
            stack.push(token)
        else: # 연산자이면
            b = stack.pop()
            a = stack.pop()     #a ? b
            if token == "+":
                stack.push( a + b )
            elif token == "-":
                stack.push( a - b )
            elif token == "*":
                stack.push( a * b )
            else:
                stack.push( a / b )
    # 스택에 남아 있는 최종 계산 결과를 반환한다.
    return stack.pop()




# 테스트 코드
if __name__ == "__main__":
    queue = Queue()
    queue.add(100)
    queue.add(200)
    queue.showList()             # 100 <-> 200
    print(queue.remove())        # 100
    queue.showList()             # 200

    # 토큰화 테스트
    expr = "3 + 5 * ( 10 - 2 )"
    tokens = Queue.toTokens(expr)
    print("Tokens:", tokens)

    # 중위 → 후위 변환 테스트
    postfix_queue = infix2Postfix(tokens)
    print("Postfix Queue:")
    postfix_queue.showList()

lst = Queue.totokens("3.4 + 35 * (45 - 23)")
print(lst)
print(stackCalculator(infix2Postfix(lst)))

