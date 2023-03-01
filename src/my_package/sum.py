class addInteger:
    
    def __init__(self,x,y):
        self.a=x
        self.b=y

    def add(self):
        return self.a + self.b
    
obj = addInteger(4,5)
print(obj.add())