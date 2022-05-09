# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
		def __init__(self, key):
				self.key = key
				self.parent = self.left = self.right = None
		def __str__(self):
				return str(self.key)

 
class Tree:
		def __init__(self):
				self.root = None
				self.size = 0

		def __len__(self):
				return self.size
			
		def preorder(self, v):
			if v != None:
				print(v,'',end='')
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
			p = self.find_loc(key)
			if p == None or p.key != key:
				v = Node(key)
				if p == None:
					self.root = v
				else:
					v.parent = p
					if p.key >= key:
						p.left = v
					else:
						p.right = v
				self.size = self.size + 1
				return v
			else:
				print("key is already in the tree!")
				return p

		def deleteByMerging(self, x):
			a, b, pt = x.left, x.right, x.parent
			if a == None: # x.left가 없는 경우
				c = b # x자리에 x.right 오기
			else: # 둘 다 있는 경우
				c = m = a # x.left가 max이면서 c(x)
				while m.right != None:
					m = m.right
				m.right = b
				if b != None: #b가 있을 때
					b.parent = m # b의 부모는 max 연결 끝

			if self.root == x: # 루트가 x면
				if c == x: # c가 x이면
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

		def deleteByCopying(self, x):
			a, b, pt = x.left, x.right, x.parent
			if a: # x.left가 있으면
				y = x.left
				while y.right:
					y = y.right # y.right의 제일 끝 찾기
				x.key = y.key # y의 값을 x 자리에 copy
				if y.left: # y.left가 있으면
					y.left.parent = y.parent # y자리에 옮기기
				if y.parent.left == y:
					y.parent.left = y.left
				else:
					y.parent.right = y.left
				del y
			elif a == None and b: # a가 없고 b가 있다면
				y = b # y는 x.right
				while y.left:
					y = y.left # y.left 제일 끝 찾기
				x.key = y.key # copy
				if y.right: # y.right에 값이 있으면
					y.right.parent = y.parent # y자리에 옮기기
				if y.parent.left == y:
					y.parent.left = y.right
				else:
					y.parent.right = y.right
				del y

			else:
				if pt == None: #부모가 없으면
					self.root = None #root가 x
				else:
					if pt.left == x:
						pt.left = None
					else:
						pt.right = None
					del x
			self.size = self.size - 1 #사이즈 조절

T = Tree()

while True:
		cmd = input().split()
		if cmd[0] == 'insert':
				v = T.insert(int(cmd[1]))
				print("+ {0} is inserted".format(v.key))
		elif cmd[0] == 'deleteC':
				v = T.search(int(cmd[1]))
				T.deleteByCopying(v)
				print("- {0} is deleted by copying".format(int(cmd[1])))
		elif cmd[0] == 'deleteM':
				v = T.search(int(cmd[1]))
				T.deleteByMerging(v)
				print("- {0} is deleted by merging".format(int(cmd[1])))
		elif cmd[0] == 'search':
				v = T.search(int(cmd[1]))
				if v == None: print("* {0} is not found!".format(cmd[1]))
				else: print(" * {0} is found!".format(cmd[1]))
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
