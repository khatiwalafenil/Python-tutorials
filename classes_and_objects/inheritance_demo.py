class Parent:
    parentVar = 100

    def __init__ (self) :
        print ("parent constructor")
    
    def parent_method(self) :
        print ("this is inside parent method")
    

class Child (Parent) :

    def __init__ (self) :
        print ("Child Constructor")
        
    def child_method (self) :
        print ("this is inside child method")


child = Child ()

print("child attribute", child.parentVar)
child.parent_method()
child.child_method()





    