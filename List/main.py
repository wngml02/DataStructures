# 노드 클래스
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
    
def add(data):
  node = head