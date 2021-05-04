class HashTable:
    def __init__(self):
        self.MAX_SIZE = 100
        self.ar = [[] for _ in range(self.MAX_SIZE)]

    def hashfunc(self, key):
        h = 0
        for c in key:
            h = h + ord(c)
        return h % 100

    def __setitem__(self, key, value):
        h = self.hashfunc(key)
        exist = False
        for idx, elem in enumerate(self.ar[h]):
            if len(elem) == 2 and elem[0] == key:
                self.ar[h][idx] = (key, value)
                exist = True
                break
        if not exist:
            self.ar[h].append((key, value))

    def __getitem__(self, key):
        h = self.hashfunc(key)
        for elem in self.ar[h]:
            if len(elem) == 2 and elem[0] == key:
                return elem[1]


    def __delitem__(self, key):
        h = self.hashfunc(key)
        for idx, elem in enumerate(self.ar[h]):
            if len(elem) == 2 and elem[0] == key:
                del self.ar[h][idx]

if __name__ == '__main__':
    ht = HashTable()
    ht['march 03'] = 27
    ht['march 30'] = 25
    ht['march 27'] = 24
    print(ht.ar)
    del ht['march 3']
    print(ht.ar)
