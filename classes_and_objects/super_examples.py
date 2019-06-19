class Parent:
    def __init__ (self) :
        print ("parent constructor")
    

class Child (Parent) :
    def __init__ (self) :
        print ("child constructor")
        super().__init__()


child = Child()
