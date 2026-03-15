class Fancy:

    def __init__(self):
        self.a = []
        self.i = 0
        self.m = 1
        self.mod = 10**9+7
        
    def append(self, val: int) -> None:
        self.a.append([val, self.m, self.i])

    def addAll(self, inc: int) -> None:
        self.i += inc

    def multAll(self, m: int) -> None:
       
        self.m = self.m * m % self.mod
        self.i = self.i * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.a):
            return -1
        v, vm, vi = self.a[idx]
        
     
        ratio = self.m * pow(vm, self.mod-2, self.mod)
        return (v * ratio + self.i - ratio * vi) % self.mod
        


