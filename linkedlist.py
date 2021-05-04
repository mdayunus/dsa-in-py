class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)


    def insert_list(self, data_list):
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count


    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        if index == self.get_length():
            print('this length used')
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


    def printll(self):
        if self.head == None:
            print('empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr = llstr + str(itr.data) + '--->'
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(89)
    ll.insert_at_begining(27)
    ll.insert_at_end(67)
    ll.insert_at_end(90)
    ll.insert_list(['apple', 'banana', 'chiku', 'd*ck'])
    ll.printll()
    # print(f'length is {ll.get_length()}')
    ll.remove_at(4)
    ll.printll()
    
    ll.insert_at(4, 'mango')
    ll.printll()
    ll.insert_at(8,'jackfruit')
    ll.printll()
    
