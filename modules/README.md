# Modules and Importing
## Modules 
Modules in Python are logical entities which can be reused in different python modules and scripts

- each file can be considered as a module
- you can import a function, class or a variable from the module

---

## Using the `import` keyword

You can use the import keyword to use a module in given code:
 
For Example in `mymodule.py` :

```
def function_in_module() :
    print ("Hey there! i am Function in my module")


class MyClass: 
    def __init__(self):
        print ("My Class")
    def doSomething(self):
        print ("Function in my class")


def someFunction1 ():
    print ("In Some Function 1")

def someFunction2 () :
    print ("In Some Function 2")

```

Lets use the module in `usemodule.py` :

```
## using the import keyword
import mymodule

## lets call the functiom
mymodule.function_in_module()


```

You can also import individual functions, vars and classes, for example:

```
# using the from.
from mymodule import MyClass

## importing muliple things from MyClass
from mymodule import someFunction1, someFunction2 # you can add as many as you want here

# lets call the functiom
mymodule.function_in_module()

myClass = MyClass ()

someFunction1 () # can be called directly, no need for myodule.someFuntion1
someFunction2 ()


```




# Packaging
## Packages
Packages are the hierarchical arrangement of modules which can be called from the "." separator.

## Declaring Package: the use of __init__.py

Lets say you have a package with following hierarchy

-org
  |--- company
         |---mypackage
               |---__init__.py
               |---module1.py
               |---module2.py

`module1.py` has the following:

```
def module1_function() :
    print ("Module 1 Function")
```

and `module2.py` has the following: 

```
def module2_function() :
    print ("Module 2 Function")
```

__init__.py initializes the module for the package to be loaded in other modules. Here mypackage is loaded as the package.

contents of __init__.py woll be something like:

```
from module1 import module1_function
from module2 import module2_function
```

similarly, you will have to create a __init__.py in company and org folders (see the GitHub code)

now if we want to use this module as a package in `usemodule.py`, lets write following code snippet:

```
from org.company.mypackage import module1_function, module2_function

module1_function()
module2_function()
```


# Namespace Bifurcation
There are cases when you need to bifurcate the global and local namespaces:
Lets see and example: 

Suppose you have following code:

```
myVar = 100

def myFunc():
    myVar = myVar + 100

print(myVar)
myFunc()
print(myVar)
```

in the above example: 

- myFunc will think it has to use the local copy of myVar
- it will give you error as it will not find declaration and we are using before it.

To solve this we need to use global namespace:

```
myVar = 100

def myFunc():
    global myVar
    myVar = myVar + 100

print(myVar)
myFunc()
print(myVar)
```

