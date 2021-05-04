class HashTable:
    def __init__(self):
        self.MAX_SIZE = 100
        self.ar = [None for _ in range(self.MAX_SIZE)]

    def hashfunc(self, key):
        h = 0
        for c in key:
            h = h + ord(c)
        return h % self.MAX_SIZE

    def __setitem__(self, key, value):
        ind = self.hashfunc(key)
        self.ar[ind] = float(value)

    def __getitem__(self, key):
        ind = self.hashfunc(key)
        return self.ar[ind]

    def __delitem__(self, key):
        ind = self.hashfunc(key)
        self.ar[ind] = None

if __name__ == '__main__':
    ht = HashTable()
    ht['march 9'] = 100
    ht['march 30'] = 27
    print(ht.ar)
    print(ht['march 03'])
    print(ht['march 30'])