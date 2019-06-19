## using the import keyword

import mymodule

## using the from.
from mymodule import MyClass

## importing muliple things from MyClass
from mymodule import someFunction1, someFunction2 # you can add as many as you want here

## lets call the functiom
mymodule.function_in_module()

myClass = MyClass ()

someFunction1 () # can be called directly, no need for myodule.someFuntion1
someFunction2 ()


from org.company.mypackage import module1_function, module2_function

module1_function()
module2_function()

myVar = 100
def myFunc():
    global myVar
    myVar=myVar+100

print (myVar)
myFunc()
print (myVar)