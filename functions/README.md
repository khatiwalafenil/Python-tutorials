# Functions: Syntax and Definitions

## Basic Syntax
 Lets see the basic syntax to declare function in python.

**use def keyword define the function. the block startts with ':' **

------

### Example:

Lets function declaration in action:

```
def function_name () :
    "Function description goes here"

    #function body

    print ("function body")

    ##return statement
    return


function_name()


```
# Calling the Functions

## Exploring the function calls

Let's see different ways in which the function can be called:

## 1. Calling function without arguments
We have seen such examples in prior cards:

```
def my_function():
    print ("something")

my_function()
```
------


## 2. Calling functions with arguments
You can declare function arguments without worring about the variable types. It will dyamically get the arg type on the runtime.

```
# lets declare the function with args
def function_with_arguments (arg1, arg2) :
    print (arg1)
    print (arg2)
    return

# call the function with arguments
function_with_arguments ("arg1","arg2")
```

-----


## 3. What happens if you call without parenthesis ?

```
function_with_arguments
## nothings gonna happen here..
```

----

## 4. Lets call function inside print

```
print (function_with_arguments("1","2"))
## sice function _with_arguments is not returnign anything, it will print none
```

----


## 5. lets put function without parenthesis in the print function

```
print (function_with_arguments)
# it will print the reference of the function. 
# you can say its refering to the reference of the function in the memory
```


# Types of Parameters

Mainly there are following types of function parameters:

1. Mandatory Parameters
2. Keyword Parameters
3. Default Parameters
4. Variable Length Parameters

Lets explore example code for each of them.

----

## 1. Mandatory Parameters
Normally parameters fo the functions are mandartory parameters in python as it is required for the caller to pass all the parameters mentioned in the function:


```
## required  arguments
def arg_function (arg) :
    a = arg
    return

# below should not work
# arg_function ()
# while below should work
arg_function(10)

```

-----

## 2. Keyword Arguments
You can add a key to the arguments. In this case, you can pass arguments in any order if the parameters are passed with the keys. For example:

```
## keyword arguments
def keyword_args (name, age):
    print (name, age)

# this is valid
keyword_args (name="John", age=12)
# and this too in valid
keyword_args (age=12,name="John")
```

-----

## 3. Default Arguments

If you set the default value of an argument, the default value will be considered by the function in case you don't pass any value to it. However, if you pass the value, it will be overridden by the default value:

```
# default arguments
def default_args(name, age=44):
    print (name, age)

default_args ("john") ## its gonna take 44 as default value for age
# or else you can override its value:
default_args("john",55)
```

-----


## 4. Variable Length Arguments
You can declare functions where the number of arguments can be dynamic at runtime. You can access those variables via an array. You can consider this analogous to the command line arguments array variable.


```
# variable length arguments
    for arg in varargs:
def var_args (arg1, *varargs):
    print (arg1)
        print (arg)

var_args (10) # atlease one argument is mandatory

var_args (20,30,40,50)
```

# Return Value

## 1. Returning some value

As in a conventional programming language, you can have a function return some value back to the caller function.

```
# Return some value
def should_return(a, b):
    c = a+b
    return c

print (should_return(1,3))

```

------

## 2. Without Return Statement
The return statement is not compulsory. You will get a 'None' result if you are trying to fetch the function return value. 

```
# Returning nothing 
def no_return(a,b):
    c = a+b

print (no_return(2,2))
## prints None
```

----

## 3. Returning Blank
You can put a blank return statement, it will return None to the caller function.

```
# lets return but... nothing!
def blank_return (a,b):
    c = a+b
    return

print (blank_return(2,2))
# once again returns None

```

-----

## 4. Returning Multiple values
This might turn shocker to programmers of c lineage... (java, js, php, etc) but you can return multiple values.

```
# return muliple values
def multi_return (a,b):
    c = a + b
    return a,b,c 

# a shocker for c programmers
print (multi_return(1,3))
```

# Pass by Value / Reference

## Pass by Value vs Pass By Reference

This is a basic concept in which needs to be understood in any programming language. If you are not aware of the concept [kindly refer it first](https://stackoverflow.com/questions/373419/whats-the-difference-between-passing-by-reference-vs-passing-by-value).

-----

## What about Python?

About Python,  I would say its Pass by Value-Reference (yeah, here we go1). 

- in case of the primitives the variable points the value.
- in case of the objects, variables point to reference of the object

So when we pass the object to the function:

- Any Changes inside the function are reflected outside the function
- *But* if we change the reference of the variable, changes made in the function will not be reflected back. Because we are changing the reference of the variable inside the function. 

----

## Example:

Let's see an example: 

```
# pass by reference, not changing the reference
def reference_test_function (mylist) :
    mylist.append (10)
    print ("List inside the function", mylist)

aList = [1,2,3,4]
reference_test_function(aList)
print ("List outside the function",aList)

```

Now let's see an example changing the reference object: 

```
# pass by reference and then changing the reference
def reference_change_function (mylist) :
    mylist = [10,20,30]
    print ("List inside the function", mylist)

aList = [1,2,3,4]
reference_change_function(aList)
print ("List outside the function",aList)
```


# Lambda Expression

## About Lambda Expression

 Lambda Expression is a Famous in functional programming. Lambda Expression is an Expression which contains arguments and inline function body to perform short repetitive utility functionalities. 

 It is generally identified as anonymous function and is invoked by using the expression signature.

## Lets see an example

Using the Lambda Expression and making a function call:

```

# referencing Lambda Expression
sum = lambda a, b : a + b

# using as a function call
print(sum(2,2))
```

Let's use this expression as an anonymous function call.

----

## Some notable points in Lambda Expressions

- LE (Lambda Expression) can take any number of arguments
- But LE can return only one value (unlike a conventional function where it can)
- LE can access variables from arg list of LE and cannot access any other variable outside its scope, not event Global variables
