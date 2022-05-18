class Node:
	  def __init__(self, key):
		  self.key = key
		  self.parent = self.left = self.right = None
		  self.height = 0  # 높이 정보도 유지함에 유의!!

	  def __str__(self):
		  return str(self.key)


class BST:
		def __init__(self):
				self.root = None
				self.size = 0
		def __len__(self):
				return self.size

		def preorder(self, v):
			if v != None:
				print(v.key, end=' ')
				self.preorder(v.left)
				self.preorder(v.right)

		def inorder(self, v):
			if v != None:
				self.inorder(v.left)
				print(v,'',end='')
				self.inorder(v.right)


		def postorder(self, v):
			if v != None:
				self.postorder(v.left)
				self.postorder(v.right)
				print(v,'',end='')
				
		def find_loc(self, key):
			if self.size == None:
				return None
			p = None
			v = self.root
			while v != None:
				if v.key == key:
					return v
				elif v.key < key:
					p = v
					v = v.right
				else:
					p = v
					v = v.left
			return p

		def search(self, key):
			p = self.find_loc(key)
			if p and p.key == key:
				return p
			else:
				return None

		def insert(self, key):
			p = self.find_loc(key) # key값인 노드 찾기
			if p == None or p.key != key: # 없으면, findloc이 부모노드를 return 했을 때 하나 만들어 주기
				v = Node(key)
				if p == None: #None이면
					self.root = v # 루트에 추가
				else: # 아니면
					v.parent = p 
					if p.key >= key:
						p.left = v
					else:
						p.right = v # 오른쪽이면 추가해야함
				self.size = self.size + 1
				return v
			else:
				print("key is already in the tree!")
				return p
			x.height = 1 + max(self.height(x.left),self.height(x.right))
				# 노드들의 height 정보 update 필요
		def deleteByMerging(self, x):
			a, b, pt = x.left, x.right, x.parent
			if a == None: # x.left가 없는 경우
				c = b # x자리에 x.right 오기
			else: # 둘 다 있는 경우
				c = m = a # x.left가 max이면서 c(x)
				while m.right != None:
					m = m.right
					self.height(x)
				m.right = b
				if b != None: #b가 있을 때
					b.parent = m # b의 부모는 max 연결 끝
					
			if self.root == x: # 루트가 x면
				if c: # c가 x이면
					c.parent = None #c의 부모가 None
				self.root = c #다시 루트는 c가 됨

			else: # 루트가 아니면
				if pt.left == x: # x의 위치가 왼쪽이면
					pt.left = c #왼쪽에 c가 들어가고
				else:
					pt.right = c #아니면 오른쪽에 들어가고 
				if c != None:
					c.parent = pt #c를 x로 완전히 만들기 위해 부모연결

			self.size = self.size - 1
			x.height = max(self.height(x.left),self.height(x.right)) +1
					# 노드들의 height 정보 update 필요

		def deleteByCopying(self, x):
			a, b, pt = x.left, x.right, x.parent
			x.height = max(self.height(x.left),self.height(x.right)) +1
			
			if a: # x.left가 없는 경우
				y = x.left
				while y.right:
					y = y.right
				x.key = y.key
				if y.left:
					y.left.parent = y.parent
				if y.parent.left == y:
					y.parent.left = y.left
				else:
					y.parent.right = y.left
				del y
			elif a == None and b:
				y = b
				while y.left:
					y = y.left
				x.key = y.key
				if y.right:
					y.right.parent = y.parent
				if y.parent.left == y:
					y.parent.left = y.right
				else:
					y.parent.right = y.right
				del y
			else:
				if pt == None:
					self.root = None
				else:
					if pt.left == x:
						pt.left = None
					else:
						pt.right = None
					del x

			self.size = self.size - 1
			
			# 노드들의 height 정보 update 필요

		def height(self, x): # 노드 x의 height 값을 리턴
				if x is None:
					return -1
				leftHeight = self.height(x.left) + 1
				rightHeight = self.height(x.right) + 1
				return max(leftHeight, rightHeight)

		def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
			if x.right != None:
				return x.right
			elif x.right == None:
				return None
			else:
				if x.parent.left == x:
					return x.parent
				else:
					return None
				# x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴

		def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
			if x.left != None:
				x.left = m = x.left
				while m.right != None:
					m = m.right
				return m
			elif x.parent.left == x and x.left == None:
				return None
			else:
				if x.parent.right == x:
					return x.parent
				else:
					return None
			# x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴

		def rotateLeft(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
			if x == None:
				return
			z = x.right
			if z == None:
				return
			b = z.left
			if x.parent != None:
				if x.parent.left == x:
					x.parent.left = z
				else:
					z.parent,right = z
			z.left = x
			x.parent = z
			x.right = b
			if b != None:
				b.parent = x
			if x == self.root:
				self.root = z
			x.height = 1 + max(self.height(x.left),self.height(x.right))
			
		def rotateRight(self, x):
			# 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
			if x == None:
				return
			a = x.left
			if a == None:
				return
			c = a.right
			a.parent = x.parent # 1번 링크 수정
			if x.parent != None:
				if x.parent.left == x:
					x.parent.left = a
				else:
					x.parent.right = a #2번 링크 수정
			a.right = x #3번 링크 수정
			x.parent = a # 4번 링크 수정
			x.left = c # 5번 링크 수정
			if c != None:
				c.parent = x # 6번 링크 수정
			if self.root == x:
				self.root = a # 루트 정보 업데이트
			x.height = 1 + max(self.height(x.left),self.height(x.right))

class AVL(BST):
		def __init__(self):
				self.root = None
				self.size = 0

		def rebalance(self, x, y, z):
					# assure that x, y, z != None
					# return the new 'top' node after rotations
					# z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음

		def insert(self, key):
				# BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면 
				# super(class_name, instance_name).method()으로 호출
				# 새로 삽입된 노드가 리턴됨에 유의!
				v = super(AVL, self).insert(key)
				# x, y, z를 찾아 rebalance(x, y, z)를 호출

				return v

		def delete(self, u): # delete the node u
				v = self.deleteByCopying(u) # 또는 self.deleteByMerging을 호출가능하다. 그러나 이 과제에서는 deleteByCopying으로 호출한다
				# height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장

				while v:
						# v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
						# z - y - x를 정한 후, rebalance(x, y, z)을 호출
						v = v.parent

T = AVL()
while True:
		cmd = input().split()
		if cmd[0] == 'insert':
				v = T.insert(int(cmd[1]))
				print("+ {0} is inserted".format(v.key))
		elif cmd[0] == 'delete':
				v = T.search(int(cmd[1]))
				T.delete(v)
				print("- {0} is deleted".format(int(cmd[1])))
		elif cmd[0] == 'search':
				v = T.search(int(cmd[1]))
				if v == None:
						print("* {0} is not found!".format(cmd[1]))
				else:
						print("* {0} is found!".format(cmd[1]))
		elif cmd[0] == 'height':
				h = T.height(T.search(int(cmd[1])))
				if h == -1:
						print("= {0} is not found!".format(cmd[1]))
				else:
						print("= {0} has height of {1}".format(cmd[1], h))
		elif cmd[0] == 'succ':
				v = T.succ(T.search(int(cmd[1])))
				if v == None:
						print("> {0} is not found or has no successor".format(cmd[1]))
				else:
						print("> {0}'s successor is {1}".format(cmd[1], v.key))
		elif cmd[0] == 'pred':
				v = T.pred(T.search(int(cmd[1])))
				if v == None:
						print("< {0} is not found or has no predecssor".format(cmd[1]))
				else:
						print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
		elif cmd[0] == 'preorder':
				T.preorder(T.root)
				print()
		elif cmd[0] == 'postorder':
				T.postorder(T.root)
				print()
		elif cmd[0] == 'inorder':
				T.inorder(T.root)
				print()
		elif cmd[0] == 'exit':
				break
		else:
				print("* not allowed command. enter a proper command!")
