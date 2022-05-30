def set_friends(x, y):
	x = Node(x)
	y = Node(y)
	
	
	
def set_enemies(x, y):

	
def are_friends(x, y):
	
	
def are_enemies(x, y):
	

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