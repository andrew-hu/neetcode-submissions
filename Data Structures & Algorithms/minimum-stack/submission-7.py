class MinStack:

    def __init__(self):
        self.a = []
        self.min = []
    def push(self, val: int) -> None:
        if self.a == []:
            self.a.append(val)
            self.min.append(val)
        else:
            if self.min[len(self.min)-1] > val:
                self.a.append(val)
                self.min.append(val)
            else:
                self.min.append(self.min[len(self.min)-1])
                self.a.append(val)

    def pop(self) -> None:
        self.a.pop()
        self.min.pop()
    def top(self) -> int:
        return(self.a[len(self.a)-1])

    def getMin(self) -> int:
        return(self.min[len(self.min)-1])
