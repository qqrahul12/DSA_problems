class maxHeap:
    def __init__(self):
        self.elements = [0]
    def parentIndex(self,i):
        return i//2
    def childrenIndex(self,i):
        return 2*i,2*i+1
    def insert(self,x):
        self.elements.append(x)
        new = len(self.elements)-1
        if len(self.elements)==2:
            return
        p = self.parentIndex(new)
        while self.elements[p]<x:
            self.elements[p],self.elements[new] = self.elements[new],self.elements[p]
            if p==1:
                return
            new = p
            p = self.parentIndex(p)
    def getMax(self):
        if len(self.elements)==1:
            return "empty"
        return self.elements[1]
    def extractMax(self):
        if len(self.elements)==1:
            return "empty"
        n = len(self.elements)-1
        mx = self.getMax()
        self.elements[1],self.elements[n] = self.elements[n], self.elements[1]
        self.elements.pop()
        n = n-1
        p = 1
        while True:
            c1,c2 = 2*p,2*p+1
            if c1>n:
                break
            elif c1==n:
                x = self.elements[p]
                y = self.elements[c1]
                self.elements[p] = max(x,y)
                self.elements[c1] = min(x,y)
                break
            else:
                x = self.elements[p]
                y = self.elements[c1]
                z = self.elements[c2]
                if x == max(x,y,z):
                    break
                elif y == max(x,y,z):
                    self.elements[p],self.elements[c1] = self.elements[c1],self.elements[p]
                    p = c1
                else:
                    self.elements[p],self.elements[c2] = self.elements[c2],self.elements[p]
                    p = c2
        return mx
class minHeap:
    def __init__(self):
        self.elements = [0]
    def parentIndex(self,i):
        return i//2
    def childrenIndex(self,i):
        return 2*i,2*i+1
    def insert(self,x):
        self.elements.append(x)
        new = len(self.elements)-1
        if len(self.elements)==2:
            return
        p = self.parentIndex(new)
        while self.elements[p]>x:
            self.elements[p],self.elements[new] = self.elements[new],self.elements[p]
            if p==1:
                return
            new = p
            p = self.parentIndex(p)
    def getMin(self):
        if len(self.elements)==1:
            return "empty"
        return self.elements[1]
    def extractMin(self):
        if len(self.elements)==1:
            return "empty"
        n = len(self.elements)-1
        mx = self.getMin()
        self.elements[1],self.elements[n] = self.elements[n], self.elements[1]
        self.elements.pop()
        n = n-1
        p = 1
        while True:
            c1,c2 = 2*p,2*p+1
            if c1>n:
                break
            elif c1==n:
                x = self.elements[p]
                y = self.elements[c1]
                self.elements[p] = min(x,y)
                self.elements[c1] = max(x,y)
                break
            else:
                x = self.elements[p]
                y = self.elements[c1]
                z = self.elements[c2]
                if x == min(x,y,z):
                    break
                elif y == min(x,y,z):
                    self.elements[p],self.elements[c1] = self.elements[c1],self.elements[p]
                    p = c1
                else:
                    self.elements[p],self.elements[c2] = self.elements[c2],self.elements[p]
                    p = c2
        return mx
h = maxHeap()
h.insert(3)
h.insert(5)
h.insert(7)
h.insert(1)
h.insert(2)
h.insert(4)
h.insert(6)
print(h.getMax())
print(h.extractMax())