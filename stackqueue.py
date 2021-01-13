class Stack:
    def __init__(self, values):
        self.values = values

    def isEmpty(self):

        return True if len(self.values) == 0 else False

    def Peek(self):

        return "Empty" if self.isEmpty() else self.values[-1]

    def Push(self, n):

        self.values.append(n)

    def Pop(self):

        return self.values.pop()


class Queue:

    def __init__(self, values):
        self.values = values

    def isEmpty(self):

        return (len(self.values) == 0)

    def Peek(self):

        return "Empty" if self.isEmpty() else self.values[0]

    def Enqueue(self, n):

        self.values.append(n)

    def Dequeue(self):

        return self.values.pop(0)


queue = Queue([1, 2, 3, 4])
stack = Stack([1, 2, 3, 4])

print(queue.Peek())
print(stack.Peek())

print(queue.Dequeue())
print(stack.Pop())

queue.Enqueue(3)
stack.Push(3)

print(queue.Peek())
print(stack.Peek())
