# What is a Class ?
A class is a blueprint to define a real-world object. In class, you declare behaviors (methods) and state (state variables) of an object. If you are not familiar with OOP concept, you should refer them first. This material deals with classes and objects in python.

----

# Defining class: the syntax
Lets declare a class representing Person object having a name and and age:

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getPersonInfo (self):
        return self.name, self.age
    
    def setAge (self, age):
        self.age = age

```

in the above code snippet, `__init__` is a constructor to the class `Person`. The `getPersonInfo` and `setAge` are the methods in the Person class which will be called by the object of the person class. 

----

# Creating a Object from the Class

```
## creating a person object with name John and age 55
person =  Person("John","55")
```

----

# Accessing member variables and functions
Lets see some code snippet how we can access the member variable and functions


```
## calling the functions
print (person.getPersonInfo())

person.setAge(44)
print (person.getPersonInfo())

print (person.age)

```

# Inheritance

Like any Language supporting OOP, Python supports inheritance of methods and variables. Python also supports multiple inheritances (of course it comes with a baggage of it).

# Example of Inheritance

Let's see a demo example of inheritance using python syntax:

## Declare the Parent Class
Let's declare a parent with class name `Parent`: 

```
class Parent:
    parentVar = 100

    def __init__ (self) :
        print ("parent constructor")
    
    def parent_method(self) :
        print ("this is inside parent method")
```

----

## The Child Class: How to inherit?

To inherit you need to mention the class you are going to inherit in the () after the class name:  

```
class Child (Parent) :

    def __init__ (self) :
        print ("Child Constructor")
        
    def child_method (self) :
        print ("this is inside child method")
```

In the above example, `Child` class is the child class of the `Parent` class (I mean are you serious ? )

----

## Lets use the child class
Let's create an instance of the child class and see **how it access the member variables and methods of the parent class**

```
child = Child ()

## accessing the parent attribute from 
## instance of child object
print("child attribute", child.parentVar)

## accessing the parent method from 
## instance of cild object
child.parent_method()

## for a change, it is also accessing 
## its own method :D
child.child_method()
```

In the above example, the child object can access the `parent_method` because of inheritance. 

# Polymorphism

Python functions are polymorphic. And when we talk about polymorphism we talk about two concepts:

1. Function Overloading
2. Function Overriding

----

# Function Overloading

- Same function name
- Different Argument List

# Function Overriding

- Same Function Name 
- Same Argument List
- Happens in Parent-child Relationship

----

# Example for Both: Overriding and Overloading
Lets see an example for both the concepts:

```
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


```

If you want to keep the variable `private` to the class, you should use the data hiding concept in python. 

You can keep the variable hidden by using the `__` (double underscore) prefix to the variable name, example: `__hiddenVar` .

Lets see and Example:

```
class SecretClass :
    __secretVar  = 10

    def __init__ (self) :
        print ("constructor of secret class")
    
 
secretObj = SecretClass ()
print (secretObj.__secretVar) ## should throw an error

``` 

We can access the parent class reference by using the Super. One of the thing which can be used for is to call the parent constructor or methods from the child class.

# Example for Super Constructor

Lets see an example where we access the Super constructor of `Parent` class from the `Child` class constructor by using the super keyword.

```
class Parent:
    def __init__ (self) :
        print ("parent constructor")
    

class Child (Parent) :
    def __init__ (self) :
        print ("child constructor")
        super().__init__()


child = Child()
```

------


**Note: there is a difference in syntax of python version 2.7 and 3.x for the access super constructor. You can refer the old manuals for the same.**

A famous trade-off of Multiple inheritances is existent in python as well. Black diamond problem is a reason why many languages (like Java) avoid multiple inheritances. But Python has its own informal was to handle it: 

---

# Black Diamond Example
Black diamond happens when a class inherits two classes which are in turn inherited by a common class. Let's see some code in action:

```
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

## try changing the sequence
class D(C,B) :
    def __init__(self):
        print(" Constructor D")
    
    # def m (self) :
    #     print ("method from D")


```

-----

# Lets see this in action in Python shell

Open the python shell on your terminal and try the following commands:

```
$ python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from black_diamond import A,B,C,D
>>> d = D()
 Constructor D
>>> d.m()
method from C
>>>
```

Now also try to change the inheritance sequence in Class D and see the difference for your self.

