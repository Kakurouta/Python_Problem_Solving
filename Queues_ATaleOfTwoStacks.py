class MyQueue(object):
    def __init__(self):
        self.Lifo = []
        self.Fifo = []

    def peek(self):
        if self.Fifo != []:
            pass
        else:
            self.Fifo = self.Lifo[::-1]
        qp = self.Fifo.pop()
        self.Fifo.append(qp)
        return qp    
        
    def pop(self):
        if self.Fifo != []:
            pass
        else:
            self.Fifo = self.Lifo[::-1]
        self.Fifo.pop()
        self.Lifo = self.Fifo[::-1]
        
    def put(self, value):
        self.Lifo.append(value)
        self.Fifo = []        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())