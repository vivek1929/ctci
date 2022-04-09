# Python program to demonstrate queue implementation
# FIFO

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class MyQueue:

    def __init__(self, data) -> None:
        self.head = Node(data)
        self.size = 1

    def enqueue(self, data):
        head = Node(data)
        head.next = self.head
        self.head = head
        self.size += 1
    
    def dequeue(self):
        if (self.size == 0):
            raise Exception("Queue is empty")
        tail = self.head
        while (tail.next.next):
            tail = tail.next
        data = tail.next.data
        tail.next = None
        self.size -= 1
        return data

    def __str__(self) -> str:
        repr  = ''
        head = self.head
        while(head):
            repr += str(head.data) + '->'
            head = head.next
        return repr[:-2]

if __name__ == '__main__':
    new_queue = MyQueue('a')
    new_queue.enqueue('b')
    new_queue.enqueue('c')

    print(new_queue.dequeue())
    print(new_queue)