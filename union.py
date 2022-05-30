class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self
#
# 4개의 연산 함수 코드 등
#
def find(x):
	while x.parent != x:
		return find(x.parent)
	return x

def set_friends(x, y):
		x = Node(x)
		y = Node(y)
		x.parent = y.parent


def set_enemies(x, y):
		x = Node(x)
		y = Node(y)
		x.parent = x
		y.parent = y

def are_friends(x, y):
		x, y = find(x), find(y)
		if x == y:
			return True
		else:
			return False

def are_enemies(x, y):
		x, y = find(x), find(y)
		if x != y:
			return True
		else:
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