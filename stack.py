from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def get_len(self):
        return len(self.container)

    def pop(self):
        if self.get_len() <= 0:
            raise Exception('cannot pop now')
        return self.container.pop()

    def peek(self):
        if self.get_len() <= 0:
            raise Exception('cannot see nothing')
        return self.container[-1]

    def printstack(self):
        stackstr = ""
        for item in self.container:
            stackstr = stackstr + str(item) + '^'
        return stackstr

if __name__ == '__main__':
    s = Stack()
    s.push(12)
    s.push(23)
    print(s.peek())
    print(s.printstack())
    s.pop()
    print(s.printstack())
    s.pop()
    print(s.peek())
    print(s.get_len())
    print(s.printstack())
    # s.pop()
            