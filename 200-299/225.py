from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sq1 = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.sq1.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        count = self.sq1.qsize()
        if count == 0:
            return False
        while count > 1:
            x = self.sq1.get()
            self.sq1.put(x)
            count -= 1
        return self.sq1.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        count = self.sq1.qsize()
        if count == 0:
            return False
        x = None
        while count:
            x = self.sq1.get()
            self.sq1.put(x)
            count -= 1
        return x


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.sq1.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()