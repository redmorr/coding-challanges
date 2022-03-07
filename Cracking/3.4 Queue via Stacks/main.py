class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, *vals):
        for v in vals:
            self.stack1.append(v)

    def pop(self):
        if not self.stack1 and not self.stack2:
            raise IndexError

        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


q = MyQueue()
q.push(1, 2, 3)
assert q.pop() == 1
assert q.pop() == 2
q.push(4)
assert q.pop() == 3
assert q.pop() == 4
q.push(5, 6)
assert q.pop() == 5
q.push(7)
assert q.pop() == 6
assert q.pop() == 7
q.push(8)
assert q.pop() == 8
