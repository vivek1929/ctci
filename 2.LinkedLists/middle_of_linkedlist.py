# Salesforce Interview Question
# Given a linked list, find the middle element of linked list in one loop
from linkedlistnode import LinkedListNode

def removeMiddle(input):
  end = input
  while (end.next != None and end.next.next != None):
    input = input.next
    end = end.next.next
  print(input.data)


if __name__ == "__main__":
    a = LinkedListNode(7)
    for each in [1, 6, 5, 4, 3, 9, 6, 0]:
        a.appendnext(each)
    out = removeMiddle(a)