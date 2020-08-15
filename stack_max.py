import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        if not self.__stack:
            self.__stack.append(a)
            self.max = a
        elif a>self.max:
            t = 2*a-self.max
            self.__stack.append(t)
            self.max = a
        else:
            self.__stack.append(a)
    def Pop(self):
        if not self.__stack:
            return None
        else:
            t = self.__stack[-1]
            self.__stack.pop()
            if t>=self.max:
                self.max = 2*self.max-t
    def Max(self):
        if self.__stack:
            return self.max
        else:
            return None

if __name__ == '__main__':
    stack = StackWithMax()

    n = int(input())
    for _ in range(n):
        query = input().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
