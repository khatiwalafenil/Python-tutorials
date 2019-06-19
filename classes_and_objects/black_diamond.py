class A :
    def __init__(self):
        print(" Constructor A")
    
    def m (self) :
        print ("method from A")

class B(A) :
    def __init__(self):
        print(" Constructor B")
    
    def m (self) :
        print ("method from B")


class C(A) :
    def __init__(self):
        print(" Constructor C")
    
    def m (self) :
        print ("method from C")


class D(C,B) :
    def __init__(self):
        print(" Constructor D")
    
    # def m (self) :
    #     print ("method from D")



