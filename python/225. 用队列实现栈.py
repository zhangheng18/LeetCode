from queue import Queue


class MyStack:
    def __init__(self):
        self.q = Queue()
        self._top_element = None

    def push(self, x: int) -> None:
        self.q.put(x)
        self._top_element = x

    def pop(self) -> int:
        # 保留最后2个
        for _ in range(self.q.qsize() - 2):
            self.q.put(self.q.get())

        # 赋值 top_element
        self._top_element = self.q.get()
        self.q.put(self._top_element)
        # 弹出
        return self.q.get()

    def top(self) -> int:
        return self._top_element

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
