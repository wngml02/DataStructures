class Node: #노드 생성 클래스
	def __init__(self, key):
		self.key = key
		self.parent = self
		
		
class union(Node): #Node클래스를 받는 union클래스
	def find(x): #x의 root 함수를 찾는 함수
		while x.parent != x:
				x = x.parent
		return x

	def set_friends(x, y):
			x = find(x)
			y = find(y) #x와 y의 루트 노드 찾기
			#아군으로 만드는 함수이기 때문에 상관없이 무조건 합집합
			if x < y:
				y.parent = x
			else:
				x.parent = y


	def set_enemies(x, y):
			x = find(x)
			y = find(y)#루트 노드 찾기
			x.parent = x
			y.parent = y #각자 루트 노드는 자기 자신으로 적군 만들기

def are_friends(x, y):
			x, y = union.find(x), union.find(y) #x와 y의 루트 노드 찾기
			if x == y: #같을 경우 아군이기에
				return True
			else: #그 외의 경우
				return False

def are_enemies(x, y):
			x, y = union.find(x), union.find(y) #x와 y 루트 노드 찾기
			if x != y: #다를 경우 적군이기에 
				return True
			else: # 그외 경우
				return False

n = int(input())

#
# 필요한 자료구조 정의
#
class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self

# 아래 코드는 가능하면 고치지 말 것!
while True:
    query, x, y = input().split()
    x, y = int(x), int(y)
    if query == 'sf':
        if are_enemies(x, y): # conflict, then print -1
            print(-1)
        else:
            set_friends(x, y)
    elif query == 'se':
        if are_friends(x, y):
            print(-1)
        else:
            set_enemies(x, y)
    elif query == 'af':
        if are_friends(x, y):
            print(1)
        else:
            print(0)
    elif query == 'ae':
        if are_enemies(x, y):
            print(1)
        else:
            print(0)
    elif query == 'exit':
        break
    else:
        print('not allowed operation')