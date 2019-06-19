# Notes on Syntax
## Syntax
Python has a easy yet typical syntax. Those who are coming from a C/Java background will have to adapt a bit and get used to a new way of coding. 

----

## Variables are case sensitive, lets see some valid and invalid variables
Following are list of some valid and invalid variables:

```
# Valid
myVar = 0
MyVar = 0
_myVar = 0 # Private
__myVar = 0 # Strongly Private
myVar__ = 0 # Special name

# Invalid
0myVar = 0
$myVar = 0
@myVar = 0
for = 0 # Reserved Keyword

```

----------

## No Braces for indicating block
Those coming for C/Java background will find it a bit awkward without {}. But we dont have braces for blocks. Instead we will have to use indentation to show the block:

```
if a>b:
    print(a)
else:
    print(b)

```

---

## Rigidly enforces line indentation:

```
if a>b:
    print(a)
    if a==0:
        print('A')
else:
   print(b)
```

----

## Too many quotes: Single Double and triple quotes

```
print('Hello')
print("Hello")
print('''Hello World''')
print("""Hello World""")
```
-----

## Hash for comment

```
# Comment
# Line1
# Line2

```


# Command line args

## The command line arguments

We can get cmd args from the Sys object. We need to import sys for that in the code.
```
import sys
```

once done, we can use `sys.argv` array for the using the arguments

------

** try this code: **

### Getting the arguments in python

```
import sys

print sys.argv

print """Or may be we can go more verbose"""

i = 0;

for arg in sys.argv :
    print i
    print ""+ arg
    i = i+1

print "done"
```
