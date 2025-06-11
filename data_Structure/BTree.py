from Queue import *                             # 큐를 사용하기 위한 외부 모듈 임포트 (levelOrder, toList 등에서 사용)

# 이진 트리 클래스 정의
class BTree:
    def __init__(self, value):                  # 노드 초기화
        self.key = value                        # 노드의 데이터 값
        self.left = None                        # 왼쪽 자식 노드
        self.right = None                       # 오른쪽 자식 노드

    def __str__(self):                          # 노드를 문자열로 출력할 때 형식 지정
        return f"[{self.key}]"

    def node(self):                             # 현재 노드와 좌우 자식의 구조를 문자열로 표현
        r = ""
        r += str(self.left) if self.left else "[None]"    # 왼쪽 자식 표현
        r += "<-" + str(self) + "->"                       # 현재 노드 표현
        r += str(self.right) if self.right else "[None]"  # 오른쪽 자식 표현
        return r

    def preOrder(self):                         # 전위 순회: Node → Left → Right
        print(self, " ", end="")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):                          # 중위 순회: Left → Node → Right
        if self.left:
            self.left.inOrder()
        print(self, " ", end="")
        if self.right:
            self.right.inOrder()

    def postOrder(self):                        # 후위 순회: Left → Right → Node
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self, " ", end="")

    def levelOrder(self):                       # 레벨 순회 (BFS 방식)
        queue = Queue()                         # 큐 생성
        queue.add(self)                         # 루트 노드 큐에 추가

        while not queue.isEmpty():              # 큐가 빌 때까지 반복
            node = queue.remove()               # 노드 꺼내기
            print(node, " ", end="")            # 노드 출력
            if node.left:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)
        print("")

    def nodeCount(self):                        # 모든 노드 수 세기 (재귀 방식)
        print(self)                             # 현재 노드 출력
        count = 1
        if self.left:
            count += self.left.nodeCount()
        if self.right:
            count += self.right.nodeCount()
        return count

    def height(self):                           # 트리의 높이 계산 (재귀)
        if self.left is None and self.right is None:
            return 1                            # 리프 노드이면 높이 1
        if self.left is None:
            return self.right.height() + 1
        if self.right is None:
            return self.left.height() + 1
        return max(self.left.height(), self.right.height()) + 1

    def isComplete(self):                       # 완전 이진 트리인지 판별
        queue = Queue()
        queue.add(self)
        danger = False                          # 자식이 하나라도 없는 노드를 발견하면 True로 변경

        while not queue.isEmpty():
            node = queue.remove()
            if node.left:
                if danger:                      # danger가 True인 후에 자식이 있는 노드가 오면 False
                    return False
                queue.add(node.left)
            else:
                danger = True

            if node.right:
                if danger:
                    return False
                queue.add(node.right)
            else:
                danger = True
        return True                             # 모든 노드 통과하면 완전 이진 트리

    def toList(self):                           # 완전 이진 트리를 리스트로 변환
        if not self.isComplete():               # 완전 이진 트리가 아니면 None 반환
            return None

        lst = [None]                            # 인덱스를 1부터 사용하기 위해 [None]으로 시작
        queue = Queue()
        queue.add(self)

        while not queue.isEmpty():              # 레벨 순서대로 노드 순회
            node = queue.remove()
            lst.append(node.key)                # 노드 키(값) 리스트에 추가
            if node.left:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)
        return lst

#===========================================================================================================
class BSTree(BTree):
    # 이진 탐색 트리에 새 키값을 가진 노드를 추가한다.
    def insert(self, value):
        if value < self.key:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTree(value)
                return 1
        elif value > self.key:
            if self.right:
                return self.right.insert(value)
            else: 
                self.right = BSTree(value)
                return 1
        else:
            return 0
        
    

#===========================================================================================================
node = BSTree(100)
node.insert(50)
node.insert(500)
node.insert(130)
node.insert(60)
node.insert(55)
node.insert(280)
node.insert(20)
node.insert(150)
node.insert(80)
node.insert(10)
node.inOrder()
# ------------------- 트리 구조 생성 예제 -------------------
# nodeA = BTree("A")
# nodeB = BTree("B")
# nodeC = BTree("C")
# nodeD = BTree("D")
# nodeE = BTree("E")
# nodeF = BTree("F")
# nodeG = BTree("G")
# nodeH = BTree("H")
# nodeI = BTree("I")

# # 트리 구조 연결
# nodeA.left  = nodeB
# nodeA.right = nodeC
# nodeB.left  = nodeD
# nodeB.right = nodeE
# nodeC.left  = nodeF
# nodeD.right = nodeG
# nodeE.left  = nodeH
# nodeE.right = nodeI

# ------------------- 함수 실행 -------------------
# print(nodeA.node())                     # 트리 구조 출력

# nodeA.preOrder()                        # 전위 순회
# print()
# nodeA.inOrder()                         # 중위 순회
# print()
# nodeA.postOrder()                       # 후위 순회
# print()
# nodeA.levelOrder()                      # 레벨 순회

# print("\n[노드 수 카운트 및 출력]")
# total = nodeA.nodeCount()               # 노드 수 세기
# print(f"\n총 노드 수: {total}")

# print(f"트리의 높이: {nodeA.height()}") # 트리 높이 출력

# print(nodeB.isComplete())               # 완전 이진 트리인지 확인
# print(nodeB.toList())                   # 리스트로 변환 결과 출력
