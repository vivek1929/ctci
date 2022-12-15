# Given a linked list, add a new node a middle of existing node
from linkedlistnode import LinkedListNode

def addBeginning(input, begin):
  head = input
  new_node = LinkedListNode(begin)
  new_node.next = input
  head = new_node
  return head


if __name__ == "__main__":
    a = LinkedListNode(7)
    for each in [1, 6, 5, 4, 3, 9, 6, 0]:
        a.appendnext(each)
    out = addBeginning(a, 11)
    while (out.next != None):
      print(out.data)
      out = out.next