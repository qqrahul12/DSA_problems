class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class list:
    def __init__(self):
        self.head = None
    def add(self,x):
        if self.head == None:
            self.head = x
        else:
            y = self.head
            while y.next:
                y = y.next
            y.next = x
    def __str__(self):
        y = self.head
        l = ""
        while y:
            l += "{} ".format(y.data)
            y = y.next
        return l
l1 = list()
h = Node(1)
l1.add(h)
for i in range(10):
    x = Node(i+1)
    l1.add(x)
print(l1)