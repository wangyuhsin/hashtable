class HashTable:
    def __init__(self, nbuckets):
        self.nbuckets = nbuckets
        self.htable = dict()
        for i in range(self.nbuckets):
            self.htable[i] = []

    def __len__(self):
        l = 0
        for i in range(len(self.htable)):
            l += len(self.htable[i])
        return l

    def __setitem__(self, key, value):
        n = 0
        for i in range(len(self.htable[hash(key) % self.nbuckets])):
            if key == self.htable[hash(key) % self.nbuckets][i][0]:
                self.htable[hash(key) % self.nbuckets][i] = (key, value)
                break
            n += 1
        if n == len(self.htable[hash(key) % self.nbuckets]):
            self.htable[hash(key) % self.nbuckets].append((key, value))

    def __getitem__(self, key):
        for i in range(len(self.htable[hash(key) % self.nbuckets])):
            if key == self.htable[hash(key) % self.nbuckets][i][0]:
                return self.htable[hash(key) % self.nbuckets][i][1]
        return None

    def __contains__(self, key):
        if key in self.keys():
            return True
        else:
            return False

    def __iter__(self):
        for key in self.keys():
            yield key

    def keys(self):
        k = []
        for item in self.items():
            k.append(item[0])
        return k

    def items(self):
        itms = []
        for i in range(self.nbuckets):
            for j in range(len(self.htable[i])):
                itms.append(self.htable[i][j])
        return itms

    def __repr__(self):
        s = ""
        for i in range(len(self.htable)):
            s += "000" + str(i) + "->"
            if len(self.htable[i]) == 0:
                s += "\n"
            for j in range(len(self.htable[i])):
                if j != (len(self.htable[i]) - 1):
                    s += (
                        str(self.htable[i][j][0])
                        + ":"
                        + str(self.htable[i][j][1])
                        + ", "
                    )
                else:
                    s += (
                        str(self.htable[i][j][0])
                        + ":"
                        + str(self.htable[i][j][1])
                        + "\n"
                    )
        return s

    def __str__(self):
        s = ""
        for i in range(len(self.htable)):
            for j in range(len(self.htable[i])):
                s += str(self.htable[i][j][0]) + ":" + \
                    str(self.htable[i][j][1]) + ", "
        return "{" + s[:-2] + "}"
