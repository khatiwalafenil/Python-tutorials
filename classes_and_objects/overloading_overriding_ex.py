class Parent:
    def overriding_function_name (self, someArg):
        print ("parent function message")
    
    def overloading_function_name(self, someArg):
        print (someArg)

    def loading_function (self, someArg1) : 
        print (someArg1)
    
    # def loading_function( self, someArg1, someArg2) :
    #     print (someArg1, someArg2)

class Child(Parent) :
    def overriding_function_name (self, someArg1):
        print ("child function message")
    
    def overloading_function_name (self) :
        print ("overloaded function name")


child = Child()

child.overriding_function_name("hello")
child.overloading_function_name()

# child.loading_function("hello")
# child.loading_function("hello", "world")


