from collections import deque
class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, data):
        self.container.appendleft(data)

    def dequeue(self):
        return self.container.pop()

    def get_len(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) > 0

    def printq(self):
        strq = ''
        for elem in self.container:
            strq =  strq + str(elem)
        return strq

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(22)
    q.dequeue()
    print(q.printq())
    