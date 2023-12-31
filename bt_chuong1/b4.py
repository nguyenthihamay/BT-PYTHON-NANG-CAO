class stack:
    def __init__(self,size):
        self.size=size
        self.data=[None]*size
        self.top=-1
    def push(self,element):
        if self.isFull():
            print("stack is full")
            return
        self.top+=1
        self.data[self.top]=element
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return -1
        element=self.data[self.top]
        self.top-=1
        return element
    def isFull(self):
        return self.top==self.size-1
    def isEmpty(self):
        return self.top==-1
Stack=stack(3)
Stack.push(3.0)
Stack.push(2.0)
Stack.push(4.0)
Stack.push(2)
print(Stack.pop())
print(Stack.pop())
