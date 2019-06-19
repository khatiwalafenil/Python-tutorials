# Control Flow

## Using If - elif and else

As in all the programming languages we gave an if-elseif and else block. Here in in python you will use `elif` for else if. 

Lets see an Example:

```
x = int(input("Please enter a number: "))
if x < 0:
     x = 0
     print('Negative changed to zero')
elif x < 100 and x>50:
    print('50 to 100')
elif x == 1:
    print('One')
else:
    print('More than 100')

```

Example output:

```
Please enter a number: 55
50 to 100
```

# Variables 
## 1. Lets explore variables
Despite of informal declaration of variables in python it is a strongly types variable. Let's explore more about it here.

---

## 2. Automatic Declaration
You just need to mention the name of the variable and assign the value and you are done. It detects the type of the variable and allocated the space and value of that value to the variable.

```
slice = 8
type = "Cheese Pizza"
is_available = True

print(slice)
print(type)
print(is_available)

```

---


## 3. Redeclaration of Variable

The variable can be redeclared (even with different type) just by assigning the value in the executable scope of code:

```
weight = 45.9
print(weight)
# This will print 45.9


weight = "Light"
print(weight)
# This will print Light

```

----

## 4. Strongly Typed property

Variables are strongly typed in contrast to the intuition we get because of the informal declaration. For example:

```
print ("foo" + "bar")

# foobar
print ("foo" + 12)
# TypeError: must be str, not int

print ("foo" + str(12))
# foo12

```

---

## 5. Global vs Local
Python maintains the scope of the global vs local variable as you might expect in any other programming language:

```
weight = "Heavy"
def firstFunction():
    weight = 90
    print(weight)


# This will print 90
firstFunction()

print(weight)
# This will print Heavy

```

----

## 6. Delete Variable

You can remove the variable from the memory during the script execution by using the del keyword :

```
weight="normal"

del weight


print(weight)
# NameError: name 'weight' is not
defined

```

# Loops

## While Loop
While loop will execute the loop until the condition is not false:

```
# using while loop

c = 0
while (c < 5):
    print (c)
    c = c + 1
```

----


## For Loop

For loop in python is best used to iterate over strings and lists.

### Iterating the String

Lets see an example where we iterate characters of strings:

```
myString = "Hello World"

for char in myString:
    print (char)

```

### Iterating the lists

```
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

for day in weekdays :
    print (day)
```

# The Range Function

## The use of Range function

The range function is used to produce a fictitious list over which the for loop can iterate. It comes with two flavors, single argument and two arguments.

### Range function with single argument

This produces list starting from index 0

```
for n in range(5): 
    print n
## prints nums 0 to 4
```

### Range function with double argument

This produces list within given range of numbers:

```
for n in range(2,5):
    print n
## prints 2 to 4
```


# Break, Contimue, pass, else in loops

## Break

As in C / C++ it stops execution of the code

## Continue

Once again derived from C, it will start next iteration of loop skipping all the code after this statement

## Pass 

The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

```
>>>while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```

This is commonly used for creating minimal classes:

```
>>>
>>> class MyEmptyClass:
...     pass
...
```

## Else in Loops

Loop statements may have an else clause: 

- it is executed when the loop terminates through exhaustion of the list (with for) or 
- when the condition becomes false (with while), 
- but not when the loop is terminated by a break statement.

Examples:


```
## using while loop with else
c = 0
while c < 4:
    print (c)
    c = c + 1
else:
   print ("end value is:", c)
# else is executed with condition becomes false

nums = [1,2,3,4,5]
for n in nums:
    print n
else: 
    print n
```



# Boilerplate code

As per suggestions by Google Python Class, its better to use this boilerplate code to emulate main function in python script.

```
import sys

def main():
    print 'Hello there', sys.argv[1]

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
```

# Sorting Examples

## Sorting using Sorted() Methods

### Normal sorted usage
Sorted function returns a list which is sorted. Note that a seperate copy is creted:

```
a = [5, 1, 4, 3]
print sorted(a)  ## [1, 3, 4, 5]
print a  ## [5, 1, 4, 3]
```

-----

### Lets Compare String

String comparisons are by default case sensitive:

```
strs = ['aa', 'BB', 'zz', 'CC']
print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
```

### Custom Sorting
Maybe you want to try sort list in reverse alphabetical order. You need to mention the custom sort order. Lets see an example:

```
print sorted(strs, reverse=True)   ## ['zz', 'aa', 'CC', 'BB']
```

Or may be we want to sort the string by the length of the strings and not the string itself: 

```
strs = ['ccc', 'aaaa', 'd', 'bb']
print sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']
```

Let's make the sort non-case-sensitive by usig str.lower customer sorting method:

```
## "key" argument specifying str.lower function to use for sorting
print sorted(strs, key=str.lower)  ## ['aa', 'BB', 'CC', 'zz']

```

>> #You can also supply your own sorting method. Put your method in key=


# List Comprehensions

## What are List Comprehensions?
A list comprehension is a compact way to write an expression that expands to a whole list

## Syntax
You write comprehensions in following syntax: 
`[ expr for var in list ]`

## Examples

Lets see an example which creates a list where each number is square of numbers in the original list:

```
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
```

or may be convert all strings to upper string:

```
strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
```

# Iterators and Generators

## Iterators 

Iterators are the one which work behind the scene to give `for` loops the values it iterates from the list, tuple, string,etc in a specific order. 

Lets see how we can define our own iterator.

We will need to declare `__iter__` and `__next__` functions. `__iter__` will identitfy the class as iterator class and `__next__` will give next item in the iteration.

Lets see an example:

```
class Reverse: 

    def __init__(self, data) :
        self.data = data
        self.index = len(data)
        
    def __iter__(self) :
        return self

    def __next__(self) :
        if (self.index==0):
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

lets use this in interactive shell:

```
>>> from generators_iterators import Reverse
>>> rev = Reverse('parth')
>>> iter (rev)
<generators_iterators.Reverse object at 0x103e5c3c8>
>>> for char in rev:
...     print(char)
...
h
t
r
a
p
>>>
```

----

## Generators

Generators are a simple and powerful tool for creating iterators.

Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example shows that generators can be trivially easy to create:

```
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
```


