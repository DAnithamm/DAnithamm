from Opps import calculator


class childImp(calculator):
    num2=300
    def __init__(self):
        calculator.__init__(self, 2, 10)
    def getcompleteData(self):
        return self.num2+self.summation()
obj = childImp()
print(obj.getcompleteData())


