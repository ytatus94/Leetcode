import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()

    def push(self, x):
        self.queue1.put(x)

    def pop(self):
        while self.queuq1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        item = self.queue1.get()
        self.quque1, self.queue2 = self.queue2, self.quque1

    def top(self):
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.push(item)
        return item

    def isEmpty(self):
        return self.queue1.empty()
