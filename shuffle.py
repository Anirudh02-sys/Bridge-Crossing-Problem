class merge:
    x = []
    y = []
    final = []

    def mergesort(self, arr):
        if len(arr) > 2:
            mid = (len(arr)+1)//2
            l = arr[:mid]
            r = arr[mid:]
            r.reverse()
            if len(l.copy()) <= 2:
                self.x .append(l.copy())
            if len(r.copy()) <= 2:
                self.y.append(r.copy())
            self.mergesort(l)
            self.mergesort(r)

    def merge(self, arr):
        spare = arr.copy()
        for i in spare:
            i.sort()
            for j in i:
                self.final.append(j)

    def shuffle(self, arr):
        self.mergesort(arr)
        self.merge(self.x)
        self.merge(self.y)
        return self.final
