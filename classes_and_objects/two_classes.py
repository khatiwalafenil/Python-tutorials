class Parent:
    def __init__(self):
        self.someVar = 10
    

class Child(Parent) :
    def __init__(self):
        super().__init__()
        self.me = 10
    
    def myFunction(self) :
        print (self.someVar)
    

c = Child()
c.myFunction()

    